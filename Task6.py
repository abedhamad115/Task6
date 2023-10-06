# Q1
print('#'*10, 'Question 1', '#'*10)
lst = [30, 75, 9, 97, 50, -4, 70, 59]
lst.sort()
print (lst[-1])
lst.remove(-4)
print (lst[0:4])
print(lst[-5:-1])
# في السؤال مطلوب طباعة اخر 4 ارقام ولكن في الأوتبوت مكتوب اول 4 ارقام لذلك طبعت كلا الأمرين
# Q2
print('#'*10, 'Question 2', '#'*10)
main_lst = [["python", 3], [5, 7.8], ["python", 11], ["python",1]]
main_lst = str(main_lst)
print(main_lst.count('python'))
# Q3
print('#'*10, 'Question 3', '#'*10)
my_lst = ["I", "LOvE", "GAZa", "sKy", "GEEks"]
print(" ".join(my_lst).lower())
# Q4
print('#'*10, 'Question 4', '#'*10)
my_lst = [12, 3.8, "GSG", ["sKy", "zak"]]
new_lst = list(my_lst)
print(new_lst)
print(id(new_lst))
print(id(my_lst))
# Q5
print('#'*10, 'Question 5', '#'*10)
my_lst = ["GSG", "zakaria", 19, 9.8, "Omar"]
lst2 = my_lst[2:]
lst2.reverse()
my_lst[2:] = lst2
print(my_lst)
#Q6
print('#'*10, 'Question 6', '#'*10)
nums = [33, 5.9, 6, -43, 9, 7, 39, 0, -40]
print(sum(nums))
#Q7
print('#'*10, 'Question 7', '#'*10)
tuple1 = (4, 'python', 'GSG', [8, 3, 1])
tuple2 = 9,
tuple = tuple1+tuple2
print(tuple)
# Q8
print('#'*10, 'Question 8', '#'*10)
tuple1 = (4, 'python', 'GSG', [8, 3, 1])
tuple2 = ('Java', 'C++', 7.8)
new_tuple = tuple1+tuple2
print(new_tuple)