# رنامه به پایتون بنویس که ورودی به شکل زیر بگیرد
# 1+1+3+1+3
# و خروجی به شکل زیر باشد 
# 1+1+1+3+3

input_str = input()

nums_list = input_str.split("+")
nums_list = [int(num) for num in nums_list]

nums_list.sort()

output_str = "+".join([str(num) for num in nums_list])

print(output_str)
