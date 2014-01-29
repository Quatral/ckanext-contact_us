import ckan.plugins as p
import ckan.plugins.toolkit as toolkit

class ContactUsPlugin(p.SingletonPlugin):
    # Declare that this class implements IConfigurer.

    p.implements(p.IRoutes, inherit=True)
    p.implements(p.IConfigurer, inherit=True)


    
    def update_config(self, config):

        # Add this plugin's templates dir to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        # 'templates' is the path to the templates dir, relative to this
        # plugin.py file.
        toolkit.add_template_directory(config, 'templates')
        
    def after_map(self, map):
        map.connect('contact_us', '/contact-us',
            controller='ckanext.contact_us.controller:ContactUsController',
            action='index')
        return map  
 
        
          