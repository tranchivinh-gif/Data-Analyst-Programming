# import numpy as np 
# # Tạo mảng 1 chiều
# a =np.array([1, 2, 3, 4, 5])
# print(a)
# print()

# # Tạo mảng 2 chiều (ma trận)
# b =np.array([[1, 2, 3], [4, 5, 6]])
# print(b)
# print()
# # # Tạo mảng toàn số 0
# zeros = np.zeros((2, 3))
# print(zeros)
# print()

# # # Tạo mảng toàn số 1
# ones = np.ones((3, 3))
# print(ones)
# print()

# # # Tạo mảng số ngẫu nhiên
# rand = np.random.rand(2, 3)
# print(rand)
# print()

# # # Tạo dãy số cách đều
# arange = np.arange(0, 10, 2) # [0,2,4,6,8]
# print(arange)
# print()

# linspace = np.linspace(0, 1, 5) # 5 số cách đều từ 0 đến 1
# print(linspace)
# print()

# print(a.shape)
# print(a.ndim)
# print(a.size)
# print(a.dtype)

# x = np.array([10, 20, 30, 40, 50])

# print(x[0])
# print(x[-1])
# print(x[1:4]) 
# print(x[:3])

# a =np.array([1, 2, 3])
# b =np.array([4, 5, 6])
# print(a + b)
# print(a- b)
# print(a * b)
# print(a / b)
# print(a ** 2)
# print(np.dot(a, b))

# arr = np.array([1, 2, 3, 4, 5])
# print(np.sum(arr))
# print(np.mean(arr))
# print(np.max(arr))
# print(np.min(arr))
# print(np.std(arr))


import pandas as pd
# s = pd.Series([0,1,2,3])
# print(s)

# A=np.array([[1, 2], [3, 4]])
# B=np.array([[2, 0], [1, 3]])
# print(np.matmul(A, B)) # nhân ma trận
# print(np.linalg.inv(A)) # ma trận nghịch đảo
# print(np.linalg.det(A)) # định thức

# # Tạo Series
# s = pd.Series([10, 20, 30, 40], index=['a','b','c','d'])
# print(s)
# # Tạo DataFrame từ dictionary
# data = {    
# 'Name': ['An', 'Bình', 'Chi'],
# 'Age': [20, 21, 19],
# 'Score': [85, 90, 88]}
# df = pd.DataFrame(data)
# print(df)

# # Tạo DataFrame
# data = {'Tên': ['An', 'Bình', 'Chi'],
# 'Tuổi': [23, 25, 22],
# 'Điểm': [8.5, 9.0, 7.8]}
# df = pd.DataFrame(data)
# # Xemdữliệu
# print(df)
# # Tính điểm trung bình
# print(df['Điểm'].mean())

# s = pd.Series([0,1,2,3])
# print(s)

# s = pd.Series([0,1,2,3], index=["a","b","c","d"])
# print(s)

# data = {'a' :-1.3, 'b' : 11.7, 'd' : 2.0, 'f': 10, 'g': 5}
# ser = pd.Series(data,index=['a','c','b','d','e','f'])
# print(ser)

# ser = pd.Series(5, index=[1, 2, 3, 4, 5])
# print(ser)

# S =pd.Series(np.random.randint(100, size = 4))
# print(S)
# print(S.index)
# print(S.values)

# chi_so = ["Ke toan", "KT", "CNTT", "Co khi"]
# gia_tri = [310, 360, 580, 340]
# S =pd.Series(gia_tri, index=chi_so)
# print(S)
# print(S.index)
# print(S.values)

# chi_so = ["KT", "KT", "CNTT", "Co khi"] # trùng nhau
# gia_tri = [310, 360, 580, 340]
# S =pd.Series(gia_tri, index=chi_so)
# print(S)
# print(S.index)
# print(S.values)

# data = {'a' : -1.3, 'b' : 11.7, 'd' : 2.0, 'f': 10, 'g': 5}
# ser = pd.Series(data,index=['a','c','b','d','e','f'])
# print(ser['d'])
# print(ser['c'])
# print(ser)

# data = {'a' : -1.3, 'b' : 11.7, 'd' : 2.0, 'f': 10, 'g': 5}
# ser = pd.Series(data,index=['a','c','b','d','e','f'])
# print(ser[:'d'])

# data = {'a' : -1.3, 'b' : 11.7, 'd' : 2.0, 'f': 10, 'g': 5}
# ser = pd.Series(data,index=['a','c','b','d','e','f'])
# print(ser[:2])

# data = {'a' : -1.3, 'b' : 11.7, 'd' : 2.0, 'f': 10, 'g': 5}
# ser = pd.Series(data,index=['a','c','b','d','e','f'])
# print(ser[-3:])
# data = {'a' : -1.3, 'b' : 11.7, 'd' : 2.0, 'f': 10, 'g': 5}
# ser = pd.Series(data,index=['a','c','b','d','e','f'])
# a = np.asarray(ser)
# print(a)

# chi_so = ["KT", "KT", "CNTT", "Co khi"] # trùng nhau
# gia_tri = [310, 360, 580, 340]
# S =pd.Series(gia_tri, index=chi_so)
# print(S['Co khi'])
# print(S['KT'])
# print(S.CNTT)
# chi_so = ["Ke toan", "KT", "CNTT", "Co khi"]
# gia_tri = [310, 360, 580, 340]
# # chỉ số giống nhau thì tính gộp, nếu không thì NaN
# S =pd.Series(gia_tri, index=chi_so)
# P=pd.Series([100, 100], ['CNTT', 'PM'])
# Y=S+P
# print(Y)

# #    S.axes: trả về danh sách các chỉ mục của S
# #    S.dtype: trả về kiểu dữ liệu các phần tử của S
# #    S.empty: trả về True nếu S rỗng
# #    S.ndim: trả về số chiều của S (1)
# #    S.size: trả về số phần tử của S
# #    S.values: trả về list các phần tử của S
# #    S.head(n): trả về n phần tử đầu tiên của S
# #    S.tail(n): trả về n phần tử cuối cùng của S
  
# def Tang(x):
#    return x if x > 500 else x+1000
# chi_so=["Ketoan","KT","CNTT","Cokhi"]
# gia_tri=[310,360,580,340]
# S=pd.Series(gia_tri,chi_so)
# #ápdụngTangtrênS(khôngthayđổiS)
# print(S.apply(Tang))
# # tạo dict từ các series
# s = {'một': pd.Series([1., 2., 3., 5.], index=['a', 'b', 'c', 'e']),
# 'hai': pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
# # tại DataFrame từ dict
# df = pd.DataFrame(s)
# print(df)

# # tạo dict từ các series
# s = {'một': pd.Series([1., 2., 3., 5.], index=['a', 'b', 'c', 'e']),
# 'hai': pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
# # tạo DataFrame từ dict theo các index được chọn
# df = pd.DataFrame(s, index=['a','c','d'])
# print(df)

# names = ['MIT',"Stanford","DHTL"]
# df = pd.DataFrame(names)
# print(df)
# names_rank=[['MIT',1],["Stanford",2],["DHTL",200]]
# df = pd.DataFrame(names_rank)
# print(df)

# crimes_rates = {
# "Year":[1960,1961,1962,1963,1964],
# "Population":[179323175,182992000,185771000,188483000,191141000],
# "Total":[3384200,3488000,3752200,4109500,4564600],
# "Violent":[288460,289390,301510,316970,364220] }
# crimes_dataframe = pd.DataFrame(crimes_rates)
# print(crimes_dataframe)
# data = [ {'MIT': 5000, 'Stanford': 4500, "DHTL":15000},
# {'MIT': 1, 'Stanford': 2, "DHTL":200} ]
# df = pd.DataFrame(data, index=['NumOfStudents', "ranking"])
# print(df)
# print(df.DHTL.dtype)

# data = { "one": pd.Series([1,23,45], index = [1,2,3]),
# "two": pd.Series([1000,2400,1132,3434], index = [1,2,3,4]) }
# df = pd.DataFrame(data)
# print(df)
# s = {'một': pd.Series([1., 2., 3., 5.], index=['a', 'b', 'c', 'e']),
# 'hai': pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd']),
# 'ba': pd.Series([9., -1.3, 3.5, 41.1], index=['a', 'b', 'c', 'd'])}
# df = pd.DataFrame(s)
# # chọn cột hai
# df_hai = df['hai']
# print(df_hai)

# s = {'một': pd.Series([1., 2., 3., 5.], index=['a', 'b', 'c', 'e']),
# 'hai': pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd']),
# 'ba': pd.Series([9., -1.3, 3.5, 41.1], index=['a', 'b', 'c', 'd'])}
# df = pd.DataFrame(s)
# # thêm cột bốn với giá trị mỗi ô theo công thức
# df_bon = df['hai'] - df['ba']
# print(df_bon)

# # thêm cột với giá trị vô hướng (scalar value)
# df['Chuẩn'] = 'OK'
# # thêm cột không cùng số lượng index với DataFrame
# df['Khác'] = df['hai'][:3]
# # thêm cột True/False theo điều kiện
# df['KT'] = df['một'] == 3.0
# # dùng hàm insert. Cột "chèn" bên dưới sẽ ở vị trí 2 (tính từ 0), có giá trị 
# bằng cột một
# df.insert(2, 'chèn', df['một'])
# print(df)

# s = {'một': pd.Series([1., 2., 3., 5.], index=['a', 'b', 'c', 'e']),
# 'hai': pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd']),
# 'ba': pd.Series([9., -1.3, 3.5, 41.1], index=['a', 'b', 'c', 'd'])}
# df = pd.DataFrame(s)
# # xóa cột hai
# del df['hai']
# # pop cột ba với dict tv_ba
# tv_ba = df.pop('ba')
# print( df)

# s = {'một': pd.Series([1., 2., 3., 5.], index=['a', 'b', 'c', 'e']),
# 'hai': pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd']),
# 'ba': pd.Series([9., -1.3, 3.5, 41.1], index=['a', 'b', 'c', 'd'])}
# df = pd.DataFrame(s)
# # chọn dòng theo label
# d = df.loc['a']
# print(d)
# s = {'một': pd.Series([1., 2., 3., 5.], index=['a', 'b', 'c', 'e']),
# 'hai': pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd']),
# 'ba': pd.Series([9., -1.3, 3.5, 41.1], index=['a', 'b', 'c', 'd'])}
# df = pd.DataFrame(s)
# # chọn dòng theo vị trí nguyên
# d = df.iloc[4] print(d)
# s = {'một': pd.Series([1., 2., 3., 5.], index=['a', 'b', 'c', 'e']),

# 'ba': pd.Series([9., -1.3, 3.5, 41.1], index=['a', 'b', 'c', 'd'])}
#  'hai': pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd']),
# # cắt lấy ra từ dòng 3 đến dòng 4
#  df = pd.DataFrame(s)
#  d = df[2:4] print(d)

# pd.read_csv(filename)
#  Cách đọc dữ liệu từ một file CSV
# pd.read_table(filename)
#  Cách đọc dữ liệu từ một file TSV
# pd.read_excel(filename)
#  Cách đọc dữ liệu từ một file Excel
# Cách đọc dữ liệu từ một cơ sở dữ liệu SQL
# pd.read_sql(query, connection_object)Cách đọc dữ liệu từ nguồn JSON (file, string hoặc URL)

# Cách đọc dữ liệu từ nguồn HTML (file, string hoặc URL)
# pd.read_json(json_string)
# Cách đọc dữ liệu từ Clipboard
# pd.read_html(url)
# Nội dung của Clipboard sẽ được chuyển tới read_table()
# pd.read_clipboard()
# pd.DataFrame(dict)
#  Cách đọc dữ liệu từ kiểu từ điển trong Python
# df = pd.read_csv("data.csv")     
 
# df.to_csv("output.csv", index=False)   # ghi file CSV
#   # đọc file CSV
# df = pd.read_excel("data.xlsx")    # đọc file Excel
# df.to_excel("output.xlsx", index=False)
# df.to_csv(filename)
#  Cách xuất dữ liệu từ DataFrame ra file CSV
# df.to_excel(filename)
#  Cách xuất dữ liệu từ DataFrame ra file Excel
# df.to_sql(table_name, connection_object)
#  Cách xuất dữ liệu từ DataFrame ra SQL
#  Cách xuất dữ liệu từ DataFrame ra JSON df.to_json(filename)
# Tạo ra một bảng gồm 23 dòng và 4 cột, được điền vào những giá trị ngẫu nhiên từ 

# pd.DataFrame(np.random.rand(23,4))

# pd.Series(my_list)
#  Cách tạo ra series từ một list
# df.index = pd.date_range( '1999/1/31', periods=df.shape[0])
#  Cách thêm index là cột ngày tháng
# Cách xem n dòng đầu tiên của DataFrame
 
# Cách xem n dòng cuối cùng của DataFrame
#  df.head(n)
# Cách lấy số dòng số cột của DataFrame
#  df.tail(n)
# Xem thông tin về Index, kiểu dữ liệu và dung lượng của DataFrame
#  df.shape

#  df.info()
# Tổng kết thông tin thống kê cho các cột có kiểu dữ liệu là số
 
# Xem giá trị duy nhất và đếm số giá trị này, đếm cả trường hợp NA
#  df.describe()
# s.value_counts(dropna=False)
#  Lưu ý Áp dụng cho đối tượng Series
#  Tổng kết giá trị duy nhất và đếm cho tất cả các cột df.apply(pd.Series.value_counts)
# Trả về một cột của DataFrame dưới dạng Series

# df[col]
#  Trả về cột có label là col như một Series
# df[[Col1, Col2]]
#  Trả về các cột trong danh sách dưới dạng một DataFrame mới
# s.iloc[0]
#  Chọn dữ liệu theo vị trí
#  Chọn dữ liệu theo index s.loc['index_one']

# df.iloc[0,:]
#  Chọn dữ liệu ở dòng đầu tiên
# df.iloc[0,0]
#  Chọn dữ liệu ở dòng đầu tiên, ô thứ nhất của DataFrame
# Đổi tên các cột trong DataFrame theo thứ tự
 
# Kiểm tra dữ liệu với giá trị null
#  df.columns = ['a','b','c']
# Kiểm tra dữ liệu với giá trị khác null
#  pd.isnull()
# pd.notnull()
# Cách bỏ toàn bộ dòng có dữ liệu null
# df.dropna()

# Cách bỏ toàn bộ cột có dữ liệu null
# df.dropna(axis=1)
# Cách bỏ các dòng có nhiều hơn n giá trị null
# df.dropna(axis=1, thresh=n)
# Cách thay toàn bộ giá trị null bằng giá trị x
# df.fillna(x)
# Cách thay toàn bộ giá trị null bằng giá trị khác
# Thay giá trị null trong Series bởi giá trị mean của các giá trị trong Series (mean có 
# thể thay được bởi các hàm khác trong module statistics của Python)
# s.fillna(s.mean())
# Cách chuyển đổi kiểu dữ liệu của Series sang Float
# s.astype(float)
# Cách thay giá trị này bởi giá trị khác
# Thay tất cả các giá trị bằng 1 bởi one
# s.replace(1,'one')
# Cách thay nhiều giá trị cùng lúc
# s.replace([1,3],['one','three'])
# Cách đổi tên cột hàng loạt bằng lambda
# df.rename(columns=lambda x: x + 1)


# Cách đổi tên cột cụ thể trong DataFrame
# df.rename(columns={'old_name': 'new_ name'})
# Cách đổi index trong DataFrame
# df.set_index('column_one')
# Cách đổi index hàng loạt trong DataFrame
# df.rename(index=lambda x: x + 1)
# Lọc dữ liệu theo điều kiện
# Lọc ra các dòng thỏa mãn điều kiện col lớn hơn 5
# df[ df[col] > 5 ]
# Lọc ra các dòng thỏa mãn điều kiện: có giá trị cột col trong khoảng 100 đến 200
# df[ df[col] > 100 & df[col] < 200 ]
# Sắp xếp dữ liệu
# Sắp xếp dữ liệu trong cột col1 theo chiều thuận (ascending)
# df.sort_values(col1)
# Sắp xếp dữ liệu trong cột col2 theo chiều nghịch (descending)
# df.sort_values(col2, ascending=False)
# Sắp xếp col1 theo chiều thuận và col2 theo chiều nghịch
# df.sort_values([col1,col2],ascending=[True,False])

# Nhóm dữ liệu, pivot dữ liệu với groupby
# Pivot dữ liệu theo col1
# df.groupby(col1)
# Pivot dữ liệu theo nhiều cột col1, col2
# Pivot dữ liệu với pivot_table trong DataFrame
# Tạo một Pivot Table, nhóm dữ liệu theo cột col1, tính mean của col2, col3
# df.pivot_table(index=col1,values=[col2,col3],aggfunc=mean)
# Tính mean của tất cả các cột
# df.apply(np.mean)
# Tính max mỗi dòng
# Áp dụng hàm np.max() cho mỗi dòng dữ liệu
# df.apply(np.max,axis=1)
# Nối dữ liệu DataFrame theo chiều dọc
# Nối các dòng của df1 xuống dưới df2 (Số lượng các cột trong 2 DataFrames này 
# phải giống nhau)
# df1.append(df2)
# Nối dữ liệu DataFrame theo chiều ngang
# Nối các cột của df1 sang phải các cột của df2 (Số lượng các dòng trong 2 
# DataFrames này phải giống nhau)
# pd.concat([df1, df2],axis=1)

# Join dữ liệu 2 DataFrames theo kiểu SQL
# df1.join(df2,on=col1,how='inner')

# Thống kê dữ liệu cho các cột số
# df.describe()
# Tính mean cho tất cả các cột
# df.mean()
# Tính correlation giữa các cột
# df.corr()
# Đếm số giá trị không null cho các cột
# df.count()

#  Tìm giá trị lớn nhất cho mỗi cột
# df.max()
# Tìm giá trị nhỏ nhất cho mỗi cột
# df.min()
# Tìm giá trị median cho mỗi cột
# df.median()
# Tìm giá trị độ lệch tiêu chuẩn cho mỗi cột
# df.std()
#  # đọc dữ liệu và quy định cột 0 dùng làm chỉ số dòng
# d =pd.read_csv("brics.csv", index_col = 0)
# print(d)
# # tính tổng của cột population, trả về tổng
# print(d.population.sum())
# # tính tổng của cột population, trả về các tổng trong quá trình cộng
# print(d.population.cumsum())


# import matplotlib.pyplot as plt
# d =pd.read_csv("brics.csv", index_col = 0)
# d.describe()
# d =pd.read_csv("brics.csv", index_col = 0)
# d.area.plot(kind='bar')
# plt.show()





