import csv
import os
from collections import namedtuple
import time
import luigi

FILE_PATH = "test_files/payment_events_mock.csv"


class FileConverter:

    def __init__(self, file_path=""):
        """
        :param file_path: the path to access the CSV file that the FileConverter should covnert
        :type file_path: string
        """
        self._file_path = file_path
        self._file_exists = os.path.isfile(file_path)

        if self._file_exists:
            with open(self._file_path, 'r') as filename:
                reader = csv.reader(filename)
                self._Row = namedtuple('Row', ' '.join(next(reader, None)))

            self._headers = list(self._Row._fields)
        else:
            print("\n File not found!")

    def get_headers(self):
        """
        :return: list of headers from the given CSV file
        """
        headers = []
        if self._file_exists:
            headers = self._headers
        return headers

    def file_to_dict_list(self):
        """
        :return: returns a list of dictionaries, where every element contains the values of a single row
        together with the respective keys
        """
        csv_dict_list = []
        if self._file_exists:
            with open(self._file_path, 'r') as filename:
                reader = csv.reader(filename)
                next(reader, None)
                for reader_row in reader:
                    csv_dict_list.append(dict(zip(self._headers, reader_row)))

        return csv_dict_list


class ReadCsvHeaders(luigi.Task):
    file_path = luigi.Parameter(default=FILE_PATH)

    def run(self):
        fc = FileConverter(self.file_path)
        server_logger.info("Creating JSON with headers")
        print fc.get_headers()
        # TODO Write the headers into a JSON file
        time.sleep(30)


class ReadCsvContents(luigi.Task):
    file_path = luigi.Parameter(default=FILE_PATH)

    def run(self):
        fc = FileConverter(self.file_path)
        server_logger.info("Creating JSON with content")
        print fc.file_to_dict_list()
        # TODO Write the content into a JSON file
        time.sleep(30)


if __name__ == '__main__':
    luigi.build([ReadCsvHeaders(), ReadCsvContents])
