def count_substring(string, sub_string):
    count = string.count(sub_string)
    return count


string = input().split()
sub_string = input().split()

count = count_substring(string, sub_string)
print(count)
