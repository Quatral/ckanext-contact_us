import ckan.lib.base as base
import ckan.lib.helpers as h
import ckan.plugins as p
import ckan.plugins.toolkit as tk
from ckan.lib.base import BaseController, config
import jinja2
from ckan.common import _, c, g, request
from validate_email import validate_email

abort = base.abort
render = base.render

class ContactUsController(BaseController):
    def index(self, context=None):
        c = p.toolkit.c
        data = request.params or {}
        errors = {}
        error_summary = {}
        print data
        print config.get('email_to');
        
        if not data == {} :
            import ckan.lib.mailer
            if data.get('contact_us.nochange') != 'http://' :
                errors['contact_us.nochange'] = [_('The value was edited')]
            if not data.get('contact_us.name') :
                errors['contact_us.name'] = [_('Missing value')]
            if not data.get('contact_us.email') :
                errors['contact_us.email'] = [_('Missing value')]
            elif not validate_email(data.get('contact_us.email')):
                errors['contact_us.email'] = [_('Invalid email')]
            if not data.get('contact_us.message') :
                errors['contact_us.message'] = [_('Missing value')]
            
            if errors == {} :
                try:
                    emails = config.get('contact_us.email') 
                    for v in emails.split(','): ckan.lib.mailer._mail_recipient('Admin',v,data.get('contact_us.name'),data.get('contact_us.email'),'Contact form',data.get('contact_us.message'))
                    h.flash_success(_('Email sent'))
                    data = {}
                except ckan.lib.mailer.MailerException:
                    raise
        #error_summary = errors
        vars = {'data': data, 'errors': errors, 'error_summary': error_summary}
        return render('ckanext/contact_us/index.html', extra_vars=vars)
    
