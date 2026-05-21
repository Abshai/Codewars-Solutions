def solution(string):
    x = list(string)
    x.reverse()
    return("".join(x))

#Optimised version
def solution(string):
    return "".join(reversed(string))

#Pythonic version using slicing
def solution(str):
  return str[::-1]
