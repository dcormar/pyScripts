class Machine:
    def __init__(self):
        self.cmd = dict()
        self._actions = [lambda x: x + 1, lambda x: 0, lambda x: x / 2, lambda x: x * 100, lambda x: x % 2]

    def command(self, cmd, num):
        self.last_cmd = cmd
        if cmd  in self.cmd:
            return self._actions[self.cmd[cmd]](num)
        else:
            self.cmd[cmd] = 0
        return self._actions[self.cmd[cmd]](num)

    def response(self,res):
        if res == False:
            self.cmd[self.last_cmd] += 1



import random

_actions =  [lambda x:x+1, lambda x:0, lambda x: x/2, lambda x: x*100, lambda x: x%2]
test.it("Should apply the num * 0 action to the command 0")
machine = Machine()

random.seed()
for i in range(0,20):
    r = machine.command(0,random.randint(0,100))
    machine.response(r==0)
    
test.assert_equals(machine.command(0,random.randint(0,100)),0)

machine = Machine()

tests=[(0, 100, 101, "Should apply the num + 1 action to the command 0"), 
    (1, 100, 0,"Should apply the num * 0 action to the command 1"), 
    (2, 100, 50,"Should apply the num / 2 action to the command 2"), 
    (3, 1, 100,"Should apply the num * 100 action to the command 3"), 
    (4, 100, 0,"Should apply the num % 2 action to the command 4")]

for i in range(0,200):
  	number = random.randint(0,100)
  	num = machine.command(i%5, number)
  	machine.response(_actions[i%5](number) == num)

for t in tests:
    test.it(t[3])
    num = machine.command(t[0], t[1])
    test.assert_equals( num , t[2])