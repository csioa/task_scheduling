import time
import luigi
import imp

PCW = imp.load_source('FileConverter', '../../python_csv_wrapper/csv_cheatsheet.py')
FILE_PATH = "test_files/payment_events_mock.csv"


class ReadCsvHeaders(luigi.Task):
    file_path = luigi.Parameter(default=FILE_PATH)

    def run(self):
        fc = PCW.FileConverter(self.file_path)
        print fc.get_headers()
        # TODO Write the headers into a JSON file
        time.sleep(30)


class ReadCsvContents(luigi.Task):
    file_path = luigi.Parameter(default=FILE_PATH)

    def run(self):
        fc = PCW.FileConverter(self.file_path)
        print fc.file_to_dict_list()
        # TODO Write the content into a JSON file
        time.sleep(30)


if __name__ == '__main__':

    luigi.build([
        ReadCsvHeaders(),
        ReadCsvContents()
    ])
