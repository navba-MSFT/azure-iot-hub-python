# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ConfigurationMetrics(Model):
    """The configuration metrics for Iot Hub devices and modules.

    :param results: The results of the metrics collection queries.
    :type results: dict[str, long]
    :param queries: The key-value pairs with queries and their identifier.
    :type queries: dict[str, str]
    """

    _attribute_map = {
        "results": {"key": "results", "type": "{long}"},
        "queries": {"key": "queries", "type": "{str}"},
    }

    def __init__(self, **kwargs):
        super(ConfigurationMetrics, self).__init__(**kwargs)
        self.results = kwargs.get("results", None)
        self.queries = kwargs.get("queries", None)
