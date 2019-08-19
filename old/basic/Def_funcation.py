#函数式编程
#未使用的思路
#求1-100的和
def sum1(start,end):
    total=0
    for x in range(start,end+1):
        total+=x
    return total
print('1-100的和：',sum1(1,100))

#平方和
def sum2(start,end):
    total=0
    for x in range(start,end+1):
        total+=x*x+1
    return total
print('1,100的平方和：',sum2(1,100))
#使用函数式编程的思想
def sum(start, end, handle):
  total = 0
  for x in range(start, end + 1):
    total += handle(x)
  return total

def identity(n):
    return n
print(sum(1,100,identity))
def square_plus(n):
    return n**2+1
print(sum(1,100,square_plus))
print('-------------------------------')
# 处理函数is_prime用于判断一个正整数是否为素数
# 如果是素数的话，则返回该数
# 否则则返回0
def is_prime(n):

  def smallest_divisor(n):
    return find_divisor(n, 2)

  def find_divisor(n, test_divisor):
    if pow(test_divisor, 2) > n:
      return n
    elif n % test_divisor == 0:
      return test_divisor
    else:
      return find_divisor(n, test_divisor + 1)

  if 1 == n:
    return 0
  elif smallest_divisor(n) == n:
    return n
  else:
    return 0

print(sum(1, 100, is_prime))