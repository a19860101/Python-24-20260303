# def test(*args):
#     # print(args)
#     for arg in args:
#         print(arg)

# test('apple','banana','cat')

# def test(*score):
    # print(score)

# test(95,90,80,65,88,15,57)

# def test(**attribute):
    # print(attribute)

# test(name='john',mail='asdf@gmail.com',age=18)

# def avg(*scores):
    # print(sum(scores))
    # print(len(scores))
    # print(sum(scores) / len(scores))

# avg(100,80,30,90,85,65,50)
def aa(*price,people):
    print(sum(price) / people)

aa(5,180,80,30,300,60,210, people=10)