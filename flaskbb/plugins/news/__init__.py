from flask.ext.plugins import connect_event

from flaskbb.plugins import FlaskBBPlugin


from .views import news, inject_news_link

__version__ = "0.1"
__plugin__ = "newsPlugin"


class newsPlugin(FlaskBBPlugin):

    name = "news Plugin"

    description = ("This Plugin provides a simple news for FlaskBB.")

    author = "sh4nks"

    license = "BSD"

    version = __version__

    settings_key = 'plugin_news'

    def setup(self):
        self.register_blueprint(news, url_prefix="/news")
        connect_event("before-first-navigation-element", inject_news_link)

    def install(self):
        pass

    def uninstall(self):
        pass
