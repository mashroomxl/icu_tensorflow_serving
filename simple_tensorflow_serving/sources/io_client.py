from simple_tensorflow_serving.conf import config
from hdfs import InsecureClient
from hdfs.ext.kerberos import KerberosClient


class HdfsClient:
    def __init__(self, host, port=50070):
        self.host = host
        self.port = port
        if 'HDFS' == config.SOURCES['model_store']:
            self.client = KerberosClient(f"http://{host}:{port}")
        else:
            self.client = InsecureClient(f"http://{host}:{port}")

    def listdir(self, dir, status=False):
        # assert os.path.isdir(dir), "expect a directory to list, but got non-directory"
        return self.client.list(dir, status)

    def read_file(self, src_path, dst_path, encoding='utf-8', offset=0, length=None, buffer_size=None,
                  chunk_size=None, delimiter=None, progress=None):
        self.client.read(src_path)
        with self.client.read(src_path) as reader:
            return reader.read()

    def download(self, src_path, dst_path):
        return self.client.download(src_path, dst_path)
