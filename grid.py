import gym
from gym.envs.classic_control import rendering
class grid(gym.Env):
    def __init__(self):
        self.viewer=rendering.Viewer(600,600)
    def render(self):
        for i in range(6):
        	line=rendering.Line((100+80*i,100),(100+80*i,500))
        	line.set_color(0,0,0)
        	self.viewer.add_geom(line)
        for i in range(6):
        	line=rendering.Line((100,100+80*i),(500,100+80*i))
        	line.set_color(0,0,0)
        	self.viewer.add_geom(line)
        l=340
        r=420
        b=340
        t=500
        cart= rendering.FilledPolygon([(l,b), (l,t), (r,t), (r,b)])
        self.viewer.add_geom(cart)
        l=100
        r=260
        b=260
        t=340
        cart= rendering.FilledPolygon([(l,b), (l,t), (r,t), (r,b)])
        self.viewer.add_geom(cart)
        l=260
        r=500
        b=100
        t=180
        cart= rendering.FilledPolygon([(l,b), (l,t), (r,t), (r,b)])
        self.viewer.add_geom(cart)
        circle=rendering.make_circle(40)
        trans=rendering.Transform(translation=(460,300))
        circle.add_attr(trans)
        self.viewer.add_geom(circle)

        return self.viewer.render()

if __name__ == '__main__':
	t=grid()
	while True:
	    t.render()
