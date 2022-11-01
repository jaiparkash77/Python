Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num = 2.5
>>> type(num)
<class 'float'>
>>> num = 5
>>> type(num)
<class 'int'>
>>> num = 6+9j
>>> type(num)
<class 'complex'>
>>> a = 2.5
>>> b = int(a)
>>> b
2
>>> type(b)
<class 'int'>
>>> c = 5
>>> d = float(c)
>>> d
5.0
>>> type(d)
<class 'float'>
>>> e = 5
>>> f = 9
>>> g = complex(e,f)
>>> g
(5+9j)
>>> type(g)
<class 'complex'>
>>> int(True)
1
>>> int(False)
0
>>> lst = [25,45,56]
>>> type(lst)
<class 'list'>
>>> s = {45,46,21}
>>> type(s)
<class 'set'>
>>> t = (77,23,44)
>>> type(t)
<class 'tuple'>
>>> str = "jai"
>>> type(str)
<class 'str'>
>>> range(10)
range(0, 10)
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(2,20,3))
[2, 5, 8, 11, 14, 17]
>>> d = {'jai':'asus', 'om':'lenovo', 'tyro': 'iphone'}
>>> d
{'jai': 'asus', 'om': 'lenovo', 'tyro': 'iphone'}
>>> d.keys()
dict_keys(['jai', 'om', 'tyro'])
>>> d.values()
dict_values(['asus', 'lenovo', 'iphone'])
>>> d['jai']
'asus'
>>> d.get('tyro')
'iphone'
>>> 