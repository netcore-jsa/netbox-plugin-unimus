from extras.plugins import PluginConfig


class UnimusIntegration(PluginConfig):
    name = "netbox_unimus"
    verbose_name = "Unimus Integration"
    description = "Integrates Netbox and Unimus"
    version = "0.1"
    author = "Michael Rhone (michael@rhone.dev)"
    author_email = "michael@rhone.dev"
    base_url = "Unimus"
    min_version = "2.9"
    required_settings = []
    default_settings = {}


config = UnimusIntegration
