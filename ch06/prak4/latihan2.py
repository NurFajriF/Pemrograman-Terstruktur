def starFormation1(n):
    m = 0
    while(m <= n):
        print('*' * m)
        m += 1
starFormation1(5)

def starFormation2(n):
    m = 0
    while(m < n):
        print('*' * n)
        n -= 1
starFormation2(5)

def starFormation3(n):
   m = 0
   for m in range(n):
       while(m <= n):
           m += 1
           print('*' * m)
      
starFormation3(5)