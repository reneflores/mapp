import ckan.plugins as p

class HawaiiThemePlugin(p.SingletonPlugin):
    p.implements(p.IConfigurable, inherit=True)
    p.implements(p.IRoutes, inherit=True)
    p.implements(p.IConfigurer, inherit=True)

    def configure(self, config):
        p.toolkit.add_resource('static', 'ckanext-hawaii')

    def update_config(self, config):
        p.toolkit.add_template_directory(config, 'templates')
