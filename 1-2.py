import random
if __name__ == '__main__':
    cnt=0
    ans = random.randint(0,9)
    print("answer is:"+str(ans))
    guess = int(input("Guess a num:"))
    cnt += 1
    while ans != guess:
        if (ans>guess):
            print("你猜的数字小于正确答案")
        else:
            print("你猜的数字大于正确答案")
        cnt += 1
        guess = int(input("Guess a num:"))
    print("你猜了"+str(cnt)+"次，猜对了，真厉害")
