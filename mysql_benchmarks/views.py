from django.shortcuts import render
import time
def test():
    time.sleep(3)
    print('1234')

# Create your views here.
if __name__ == "__main__":
    import cProfile

    # 直接把分析结果打印到控制台
    cProfile.run("test()")
    # 把分析结果保存到文件中
    cProfile.run("test()", filename="result.out")
    # 增加排序方式
    cProfile.run("test()", filename="result.out", sort="cumulative")