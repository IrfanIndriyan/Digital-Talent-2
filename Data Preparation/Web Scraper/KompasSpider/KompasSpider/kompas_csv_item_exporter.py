from scrapy.conf import settings
from scrapy.contrib.exporter import CsvItemExporter

class KompasCsvItemExporter(CsvItemExporter):
	"""docstring for KompasCsvItemExporter"""
	def __init__(self, *args, **kwargs):
		delimiter = settings.get("CSV_DELIMITER", ',')
		kwargs['delimiter'] = delimiter

		field_to_export = settings.get("FIELD_TO_EXPORT", [])

		if field_to_export:
			kwargs['field_to_export'] = field_to_export

		super(KompasCsvItemExporter, self).__init__(*args, **kwargs)
		