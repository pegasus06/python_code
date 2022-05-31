# 日期：2022年05月17日
import yaml
class YamlUtil:
    def __init__(self,yaml_file):
        """通过init方法把yaml文件传入这个类
        :param yaml_file"""
        self.yaml_file=yaml_file
    #读取文件
    def read_yaml(self):
        """
        读取yaml，对yaml反序列化（将yaml格式转换为dict格式）
        :return:
        """
        with open(self.yaml_file,encoding="utf-8")as f:
            value=yaml.load(f,Loader=yaml.FullLoader)
            print(value,type(value))
if __name__ == '__main__':
    YamlUtil(r"E:\Python_home\py_test\api_testcase\test_api.yml").read_yaml()