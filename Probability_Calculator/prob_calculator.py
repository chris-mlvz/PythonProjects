import copy
import random
# Consider using the modules imported above.

class Hat():
    
    def __init__(self, **kwargs):
        self.contents = []
    
        for name in kwargs:
            for _ in range(kwargs[name]):
                self.contents.append(name)
    
    def draw(self, number_of_balls):
        list_of_balls = []
        
        # if draw exceeds the available quantity, return all the balls.
        if number_of_balls > len(self.contents):
            number_of_balls = len(self.contents)

        # List draw balls and remove existing balls
        for i in range(number_of_balls):
            random_value = random.randrange(len(self.contents))
            if self.contents:
                list_of_balls.append(self.contents.pop(random_value))
            else:
                break
        return list_of_balls



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count_success = 0
    for i in range(num_experiments):
        #Deepcopy hat
        hat_copy = copy.deepcopy(hat)
        #Variables
        dict_balls_draw = dict()
        ball_success = 0

        #Counting draw balls
        for ball in hat_copy.draw(num_balls_drawn):
            dict_balls_draw[ball] = dict_balls_draw.get(ball, 0) + 1

        #Comparing that we get at least "expected balls"
        for ball_expected in expected_balls:
            for ball_draw in dict_balls_draw:
                if ball_draw == ball_expected:
                    if dict_balls_draw[ball_draw] >= expected_balls[ball_expected]:
                        ball_success += 1

        #Counting if we success all expected balls
        if ball_success == len(expected_balls):
            count_success +=1

    #Probability
    probability = round(count_success/num_experiments,4)

    return probability



# hat = Hat(blue=3,red=2,green=6)
# #print(hat.contents)
# probability = experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=1000)
# actual = probability
# expected = 0.272
# # assertAlmostEqual(actual, expected, delta = 0.01, msg = 'Expected experiment method to return a different probability.')
# # hat = Hat(yellow=5,red=1,green=3,blue=9,test=1)
# # # print(hat.contents)s
# # probability = experiment(hat=hat, expected_balls={"yellow":2,"blue":3,"test":1}, num_balls_drawn=20, num_experiments=100)
# # actual = probability
# # expected = 1.0
# #assertAlmostEqual(actual, expected, delta = 0.01, msg = 'Expected experiment method to return a different probability.')

# print(actual)
# print(expected)
# if actual == expected:
#     print("Yeah")
# else:
#     print("No")