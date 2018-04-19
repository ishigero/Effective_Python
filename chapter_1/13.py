# coding: utf-8

def main():
  normal_sample()
  print('////////////')
  exception_sample()

# try
# no problem
# finish
# ////////////
# exception
# finish


def exception_sample():
  try:
    open('/hoge.txt')

  except:
    print('exception') 

  else:
    print('no problem')

  finally:
    print('finish')


def normal_sample():
  try:
    print('try')

  except:
    print('exception') 

  else:
    print('no problem')

  finally:
    print('finish')


if __name__ == '__main__':
  main()