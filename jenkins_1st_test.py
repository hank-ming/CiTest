import requests
import time
import datetime
import HTMLReport
import unittest
from HTMLReport import GeneralLogger
import random
import logging
import re
import xmlrunner


date = str(time.asctime(time.localtime(time.time())))
today = str(datetime.date.today())
date_new = ''.join(e for e in date if e.isalnum())
date_new = date_new[:-6]
print(date)
print(today)
base_url = 'https://api1.esgo.com/'

class home_page_Test(unittest.TestCase):
    def test_Case1_Check_Today_SeriesList(self):
        request_API = 'Series_List_Get'
        url = base_url + request_API
        querystring = {"date": today, "game_id": "0", "limit": "200"}  # 登入使用參數
        html = requests.request("head", url, params=querystring) # 获取封包header
        with self.subTest():
            self.assertEqual(html.status_code, 200, '回传HTTP状态码不正确') # 检查HTTP状态码
        response = requests.request("GET", url, params=querystring, timeout=3) # 发送get请求
        res_time=response.elapsed.total_seconds()
        with self.subTest():  # 检查res_time < 3秒
                self.assertLess(res_time, 3, '请求时间过长')
        retcode = response.json() # 获取接口json格式资料
        with self.subTest():
            self.assertEqual(retcode["code"], 1, '回传状态码不正确')  # 检查return code, 透过dict的方式抓取回应
            GeneralLogger().get_logger().info('============================================================数值开始============================================================')
            GeneralLogger().get_logger().info('请求API为: ' + str(response.url))
            GeneralLogger().get_logger().info("请求时间长为 " + str(res_time))
            GeneralLogger().get_logger().info('请求结果为: ' + str(retcode))
            GeneralLogger().get_logger().info('============================================================数值结束============================================================')
            GeneralLogger().get_logger().info('')

        querystring = {"date": today, "game_id": "0", "limit": "200", "status": "2"}  # 登入使用參數
        html = requests.request("head", url, params=querystring)  # 获取封包header
        with self.subTest():
            self.assertEqual(html.status_code, 200, '回传HTTP状态码不正确')
        response = requests.request("GET", url, params=querystring, timeout=3) # 发送get请求
        res_time=response.elapsed.total_seconds()
        retcode = response.json() # 获取接口json格式资料
        GeneralLogger().get_logger().info(
            '============================================================数值开始============================================================')
        GeneralLogger().get_logger().info('请求API为: ' + str(response.url))
        GeneralLogger().get_logger().info("请求时间长为 " + str(res_time))
        GeneralLogger().get_logger().info('请求结果为: ' + str(retcode))
        GeneralLogger().get_logger().info(
            '============================================================数值结束============================================================')
        GeneralLogger().get_logger().info('')
        with self.subTest():  # 检查res_time < 3秒
                self.assertLess(res_time, 3, '请求时间过长')
        with self.subTest():
            self.assertEqual(retcode["code"], 1, '回传状态码不正确')

    def test_Case2_Check_Home_Page_Top(self):
        request_API = 'Tournament_Recommend_Get'
        url = base_url + request_API

        querystring = {"limit": "50"}
        html = requests.request("head", url, params=querystring)  # 获取封包header
        with self.subTest():
            self.assertEqual(html.status_code, 200, '回传HTTP状态码不正确')  # 检查HTTP状态码
        response = requests.request("GET", url, params=querystring, timeout=3)  # 发送get请求
        print('请求API为: ' + str(response.url))
        res_time = response.elapsed.total_seconds()
        with self.subTest():  # 检查res_time < 3秒
            self.assertLess(res_time, 3, '请求时间过长')
        print("请求时间长为 " + str(res_time))  # 获取请求时间, 单位s
        retcode = response.json()  # 获取接口json格式资料
        with self.subTest():
            self.assertEqual(retcode["code"], 1, '回传状态码不正确')  # 检查return code, 透过dict的方式抓取回应
            GeneralLogger().get_logger().info('============================================================数值开始============================================================')
            GeneralLogger().get_logger().info('请求API为: ' + str(response.url))
            GeneralLogger().get_logger().info("请求时间长为 " + str(res_time))
            GeneralLogger().get_logger().info('请求结果为: ' + str(retcode))
            GeneralLogger().get_logger().info('============================================================数值结束============================================================')
            GeneralLogger().get_logger().info('')

    def test_Case3_Check_Article_List(self):
        request_API = 'Article_List_Get'
        url = base_url + request_API

        querystring = {"channel": "26"}
        html = requests.request("head", url, params=querystring)  # 获取封包header
        with self.subTest():
            self.assertEqual(html.status_code, 200, '回传HTTP状态码不正确')  # 检查HTTP状态码
        response = requests.request("GET", url, params=querystring, timeout=3)  # 发送get请求
        print('请求API为: ' + str(response.url))
        res_time = response.elapsed.total_seconds()
        with self.subTest():  # 检查res_time < 3秒
            self.assertLess(res_time, 3, '请求时间过长')
        print("请求时间长为 " + str(res_time))  # 获取请求时间, 单位s
        retcode = response.json()  # 获取接口json格式资料
        with self.subTest():
            self.assertEqual(retcode["code"], 1, '回传状态码不正确')  # 检查return code, 透过dict的方式抓取回应
            GeneralLogger().get_logger().info('============================================================数值开始============================================================')
            GeneralLogger().get_logger().info('请求API为: ' + str(response.url))
            GeneralLogger().get_logger().info("请求时间长为 " + str(res_time))
            GeneralLogger().get_logger().info('请求结果为: ' + str(retcode))
            GeneralLogger().get_logger().info('============================================================数值结束============================================================')
            GeneralLogger().get_logger().info('')

        querystring = {"channel": "18", "limit": "7"}
        html = requests.request("head", url, params=querystring)  # 获取封包header
        with self.subTest():
            self.assertEqual(html.status_code, 200, '回传HTTP状态码不正确')  # 检查HTTP状态码
        response = requests.request("GET", url, params=querystring, timeout=3)  # 发送get请求
        print('请求API为: ' + str(response.url))
        res_time = response.elapsed.total_seconds()
        with self.subTest():  # 检查res_time < 3秒
            self.assertLess(res_time, 3, '请求时间过长')
        print("请求时间长为 " + str(res_time))  # 获取请求时间, 单位s
        retcode = response.json()  # 获取接口json格式资料
        with self.subTest():
            self.assertEqual(retcode["code"], 1, '回传状态码不正确')  # 检查return code, 透过dict的方式抓取回应
            GeneralLogger().get_logger().info('============================================================数值开始============================================================')
            GeneralLogger().get_logger().info('请求API为: ' + str(response.url))
            GeneralLogger().get_logger().info("请求时间长为 " + str(res_time))
            GeneralLogger().get_logger().info('请求结果为: ' + str(retcode))
            GeneralLogger().get_logger().info('============================================================数值结束============================================================')
            GeneralLogger().get_logger().info('')

        querystring = {"channel": "27", "limit": "1"}
        html = requests.request("head", url, params=querystring)  # 获取封包header
        with self.subTest():
            self.assertEqual(html.status_code, 200, '回传HTTP状态码不正确')  # 检查HTTP状态码
        response = requests.request("GET", url, params=querystring, timeout=3)  # 发送get请求
        print('请求API为: ' + str(response.url))
        res_time = response.elapsed.total_seconds()
        with self.subTest():  # 检查res_time < 3秒
            self.assertLess(res_time, 3, '请求时间过长')
        print("请求时间长为 " + str(res_time))  # 获取请求时间, 单位s
        retcode = response.json()  # 获取接口json格式资料
        with self.subTest():
            self.assertEqual(retcode["code"], 1, '回传状态码不正确')  # 检查return code, 透过dict的方式抓取回应
            GeneralLogger().get_logger().info('============================================================数值开始============================================================')
            GeneralLogger().get_logger().info('请求API为: ' + str(response.url))
            GeneralLogger().get_logger().info("请求时间长为 " + str(res_time))
            GeneralLogger().get_logger().info('请求结果为: ' + str(retcode))
            GeneralLogger().get_logger().info('============================================================数值结束============================================================')
            GeneralLogger().get_logger().info('')


        # 抓取最新预测dota的文章
        querystring = {"type": "2", "limit": "5", "game_ids": "0", "order": "create_time desc"}
        html = requests.request("head", url, params=querystring)  # 获取封包header
        with self.subTest():
            self.assertEqual(html.status_code, 200, '回传HTTP状态码不正确')  # 检查HTTP状态码
        response = requests.request("GET", url, params=querystring, timeout=3)  # 发送get请求
        print('请求API为: ' + str(response.url))
        res_time = response.elapsed.total_seconds()
        with self.subTest():  # 检查res_time < 3秒
            self.assertLess(res_time, 3, '请求时间过长')
        print("请求时间长为 " + str(res_time))  # 获取请求时间, 单位s
        retcode = response.json()  # 获取接口json格式资料
        with self.subTest():
            self.assertEqual(retcode["code"], 1, '回传状态码不正确')  # 检查return code, 透过dict的方式抓取回应
            GeneralLogger().get_logger().info('============================================================数值开始============================================================')
            GeneralLogger().get_logger().info('请求API为: ' + str(response.url))
            GeneralLogger().get_logger().info("请求时间长为 " + str(res_time))
            GeneralLogger().get_logger().info('请求结果为: ' + str(retcode))
            GeneralLogger().get_logger().info('============================================================数值结束============================================================')
            GeneralLogger().get_logger().info('')

        # 抓取最新预测dota的文章
        querystring = {"type": "6", "limit": "5", "game_ids": "0", "order": "create_time desc"}
        html = requests.request("head", url, params=querystring)  # 获取封包header
        with self.subTest():
            self.assertEqual(html.status_code, 200, '回传HTTP状态码不正确')  # 检查HTTP状态码
        response = requests.request("GET", url, params=querystring, timeout=3)  # 发送get请求
        print('请求API为: ' + str(response.url))
        res_time = response.elapsed.total_seconds()
        with self.subTest():  # 检查res_time < 3秒
            self.assertLess(res_time, 3, '请求时间过长')
        print("请求时间长为 " + str(res_time))  # 获取请求时间, 单位s
        retcode = response.json()  # 获取接口json格式资料
        with self.subTest():
            self.assertEqual(retcode["code"], 1, '回传状态码不正确')  # 检查return code, 透过dict的方式抓取回应
            GeneralLogger().get_logger().info('============================================================数值开始============================================================')
            GeneralLogger().get_logger().info('请求API为: ' + str(response.url))
            GeneralLogger().get_logger().info("请求时间长为 " + str(res_time))
            GeneralLogger().get_logger().info('请求结果为: ' + str(retcode))
            GeneralLogger().get_logger().info('============================================================数值结束============================================================')
            GeneralLogger().get_logger().info('')

        querystring = {"type": "7", "limit": "5", "game_ids": "0", "order": "create_time desc"}
        html = requests.request("head", url, params=querystring)  # 获取封包header
        with self.subTest():
            self.assertEqual(html.status_code, 200, '回传HTTP状态码不正确')  # 检查HTTP状态码
        response = requests.request("GET", url, params=querystring, timeout=3)  # 发送get请求
        print('请求API为: ' + str(response.url))
        res_time = response.elapsed.total_seconds()
        with self.subTest():  # 检查res_time < 3秒
            self.assertLess(res_time, 3, '请求时间过长')
        print("请求时间长为 " + str(res_time))  # 获取请求时间, 单位s
        retcode = response.json()  # 获取接口json格式资料
        with self.subTest():
            self.assertEqual(retcode["code"], 1, '回传状态码不正确')  # 检查return code, 透过dict的方式抓取回应
            GeneralLogger().get_logger().info('============================================================数值开始============================================================')
            GeneralLogger().get_logger().info('请求API为: ' + str(response.url))
            GeneralLogger().get_logger().info("请求时间长为 " + str(res_time))
            GeneralLogger().get_logger().info('请求结果为: ' + str(retcode))
            GeneralLogger().get_logger().info('============================================================数值结束============================================================')
            GeneralLogger().get_logger().info('')

        # 抓取情报中心dota的文章
        querystring = {"limit": "10", "page": "1", "type": "0"}
        html = requests.request("head", url, params=querystring)  # 获取封包header
        with self.subTest():
            self.assertEqual(html.status_code, 200, '回传HTTP状态码不正确')  # 检查HTTP状态码
        response = requests.request("GET", url, params=querystring, timeout=3)  # 发送get请求
        print('请求API为: ' + str(response.url))
        res_time = response.elapsed.total_seconds()
        with self.subTest():  # 检查res_time < 3秒
            self.assertLess(res_time, 3, '请求时间过长')
        print("请求时间长为 " + str(res_time))  # 获取请求时间, 单位s
        retcode = response.json()  # 获取接口json格式资料
        with self.subTest():
            self.assertEqual(retcode["code"], 1, '回传状态码不正确')  # 检查return code, 透过dict的方式抓取回应
            GeneralLogger().get_logger().info('============================================================数值开始============================================================')
            GeneralLogger().get_logger().info('请求API为: ' + str(response.url))
            GeneralLogger().get_logger().info("请求时间长为 " + str(res_time))
            GeneralLogger().get_logger().info('请求结果为: ' + str(retcode))
            GeneralLogger().get_logger().info('============================================================数值结束============================================================')
            GeneralLogger().get_logger().info('')

    def test_Case4_Check_Tournament_List_Get(self):
        request_API = 'Tournament_List_Get'
        url = base_url + request_API
        querystring = {"game_id": "1", "limit":"36","page":"1"}
        html = requests.request("head", url, params=querystring)  # 获取封包header
        with self.subTest():
            self.assertEqual(html.status_code, 200, '回传HTTP状态码不正确')  # 检查HTTP状态码
        response = requests.request("GET", url, params=querystring, timeout=3)  # 发送get请求
        print('请求API为: ' + str(response.url))
        res_time = response.elapsed.total_seconds()
        with self.subTest():  # 检查res_time < 3秒
            self.assertLess(res_time, 3, '请求时间过长')
        print("请求时间长为 " + str(res_time))  # 获取请求时间, 单位s
        retcode = response.json()  # 获取接口json格式资料
        with self.subTest():
            self.assertEqual(retcode["code"], 1, '回传状态码不正确')  # 检查return code, 透过dict的方式抓取回应
            GeneralLogger().get_logger().info('============================================================数值开始============================================================')
            GeneralLogger().get_logger().info('请求API为: ' + str(response.url))
            GeneralLogger().get_logger().info("请求时间长为 " + str(res_time))
            GeneralLogger().get_logger().info('请求结果为: ' + str(retcode))
            GeneralLogger().get_logger().info('============================================================数值结束============================================================')
            GeneralLogger().get_logger().info('')

    def test_Case5_Check_Article_List_Get_News_page(self):
        request_API = 'Article_List_Get'
        url = base_url + request_API


        for i in range(10):

            querystring = {"channel": "1", "limit":"10","page":"1","type":i}
            html = requests.request("head", url, params=querystring)  # 获取封包header
            with self.subTest():
                self.assertEqual(html.status_code, 200, '回传HTTP状态码不正确')  # 检查HTTP状态码
            response = requests.request("GET", url, params=querystring, timeout=3)  # 发送get请求
            print('请求API为: ' + str(response.url))
            res_time = response.elapsed.total_seconds()
            with self.subTest():  # 检查res_time < 3秒
                self.assertLess(res_time, 3, '请求时间过长')
            print("请求时间长为 " + str(res_time))  # 获取请求时间, 单位s
            retcode = response.json()  # 获取接口json格式资料
            with self.subTest():
                self.assertEqual(retcode["code"], 1, '回传状态码不正确')  # 检查return code, 透过dict的方式抓取回应
            GeneralLogger().get_logger().info('============================================================数值开始============================================================')
            GeneralLogger().get_logger().info('请求API为: ' + str(response.url))
            GeneralLogger().get_logger().info("请求时间长为 " + str(res_time))
            GeneralLogger().get_logger().info('请求结果为: ' + str(retcode))
            GeneralLogger().get_logger().info('============================================================数值结束============================================================')
            GeneralLogger().get_logger().info('')
            # GeneralLogger().get_logger().info('============================================================数值开始============================================================')
            # GeneralLogger().get_logger().info('请求结果为: ' + str(retcode))
            # GeneralLogger().get_logger().info('============================================================数值结束============================================================')
            # GeneralLogger().get_logger().info('')





if __name__ == '__main__':

    # suite = unittest.TestSuite()
    # loader = unittest.TestLoader()
    # suite.addTests(loader.loadTestsFromTestCase(home_page_Test))

    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(home_page_Test))
    runner = xmlrunner.XMLTestRunner(output='report')  # 指定報告放的目錄
    runner.run(test_suite)

# 测试用例执行器
# runner = HTMLReport.TestRunner(report_file_name="test_"+ date_new,  # 报告文件名，如果未赋值，将采用“test+时间戳”
#                                output_path='report',  # 保存文件夹名，默认“report”
#                                title='测试报告',  # 报告标题，默认“测试报告”
#                                description='无测试描述',  # 报告描述，默认“测试描述”
#                                thread_count=3,  # 并发线程数量（无序执行测试），默认数量 1
#                                thread_start_wait=3,  # 各线程启动延迟，默认 0 s
#                                sequential_execution=False,  # 是否按照套件添加(addTests)顺序执行，
#                                # 会等待一个addTests执行完成，再执行下一个，默认 False
#                                # 如果用例中存在 tearDownClass ，建议设置为True，
#                                # 否则 tearDownClass 将会在所有用例线程执行完后才会执行。
#                                # lang='en'
#                                lang='cn'  # 支持中文与英文，默认中文
#                                )
# # 执行测试用例套件
# runner.run(suite)
