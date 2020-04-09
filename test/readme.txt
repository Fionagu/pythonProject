#生成测试报告
> pip install -U pytest-tml
> pytest --html=report.html

#多线程
> pip install -U pytest-xdist
> pytest -n NUM

#重跑fail的case
> pip install -U pytest-rerunfailures
> pytest --reruns NUM

#如何执行
> pytest 
# will run all tests under pythonhellon

>pytest ./test_1
# will run all tests under fodler test_1

> pytest test_sample_1.py
# will run all tests in test_sample_1.py

> pytest test_sample::test_answer_negivate
# will run test test_answer_negivate


> pytest test_sample_2.py::TestMyClass::test_method_simple
# will run test_method_simple

>pytest -k "answer and not positive"
# will run test_answer_negivate 