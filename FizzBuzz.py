def fizzBuzz(num):
    #i starts from 1 to num
    for i in range(1, num+1):

        #number divisible by 15, (divisible by both 3 & 5)
        #print 'FizzBuzz' in place of the number
        if (i % 15 == 0):
            print('FizzBuzz')
        
        #number divisible by 3
        #print 'Fizz' in place of the number
        elif(i % 3 == 0):
            print('Fizz')

        #number divisible by 5
        #print 'Buzz' in place of the number
        elif(i % 5 == 0):
            print('Buzz')
        
        #print the number
        else:
            print(i)

fizzBuzz(20)