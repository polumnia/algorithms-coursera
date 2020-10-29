# https://algs4.cs.princeton.edu/61event/CollisionSystem.java.html
import sys
import math
import heapq

import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Particle:
    def __init__(self, rx, ry, vx, vy, radius, mass):
        self.rx = rx
        self.ry = ry
        self.vx = vx
        self.vy = vy
        self.radius = radius
        self.mass = mass
        self.count = 0
    
    def move(self, dt):
        self.rx += self.vx * dt
        self.ry += self.vy * dt

    def time_to_hit(self, that):
        if self == that:
            return math.inf
        
        dx = that.rx - self.rx
        dy = that.ry - self.ry

        dvx = that.vx - self.vx
        dvy = that.vy - self.vy

        dvdr = dx * dvx + dy * dvy
        if dvdr > 0:
            return math.inf
        
        dvdv = dvx * dvx + dvy * dvy
        drdr = dx * dx + dy * dy

        sigma = self.radius + that.radius
        d = (dvdr * dvdr) - dvdv * (drdr - sigma * sigma)
        if d < 0:
            return math.inf
        return -(dvdr + math.sqrt(d)) / dvdv

    def time_to_hit_vertical_wall(self):
        if self.vx > 0:
            return (1 - self.radius - self.rx) / self.vx
        elif self.vx < 0:
            return (self.radius + self.rx) / self.vx
        else:
            return math.inf

    def time_to_hit_horizontal_wall(self):
        if self.vy > 0:
            return (1 - self.radius - self.ry) / self.vy
        elif self.vy < 0:
            return (self.radius + self.rx) / self.vy
        else:
            return math.inf

    def bounce_off(self, that):
        dx = that.rx - self.rx
        dy = that.ry - self.ry

        dvx = that.vx - self.vx
        dvy = that.vy - self.vy

        dvdr = dx * dvx + dy * dvy
        dist = self.radius + that.radius

        J = 2 * self.mass * that.mass * dvdr /((self.mass + that.mass) * dist)
        Jx = J * dx / dist
        Jy = J * dy / dist

        self.vx += Jx / self.mass
        self.vy += Jy / self.mass

        that.vx -= Jx / that.mass
        that.vy -= Jy / that.mass

        self.count += 1
        that.count += 1


    def bounce_off_vertical_wall(self):
        self.vx = -self.vx
        self.count += 1

    def bounce_off_horizontal_wall(self):
        self.vy = -self.vy
        self.count += 1
    
    def kinetic_energy(self):
        return 0.5 * self.mass * (self.vx * self.vx + self.vy * self.vy) 


class Event:
    def __init__(self, time, particle_a, particle_b):
        self.time = time
        self.a = particle_a
        self.b = particle_b
        self.count_a = 0
        self.count_b = 0
    
    def is_valid(self):
        if self.a and self.a.count != self.count_a:
            return False
        if self.b and self.b.count != self.count_b:
            return False
        return True
    
    def __lt__(self, other):
        return self.time < other.time


class CollisionSystem:
    def __init__(self, particles):
        plt.ion()
        self.pq = []
        self.t = 0.0
        self.particles = particles
        self.fig, self.ax = plt.subplots()
        self.points = self.ax.scatter(*particles_to_coordinates(self.particles))
    
    def predict(self, particle):
        if not particle:
            return
        
        for p in self.particles:
            dt = particle.time_to_hit(p)
            heapq.heappush(self.pq, (self.t + dt, Event(self.t + dt, particle, p)))
        
        heapq.heappush(
            self.pq, (
                self.t + particle.time_to_hit_vertical_wall(),
                Event(self.t + particle.time_to_hit_vertical_wall(), particle, None)
            )
        )

        heapq.heappush(
            self.pq, (
                self.t + particle.time_to_hit_horizontal_wall(),
                Event(self.t + particle.time_to_hit_horizontal_wall(), None, particle)
            )
        )
    
    def simulate(self):
        for p in self.particles:
            self.predict(p)
        heapq.heappush(self.pq, (0, Event(0, None, None)))

        while heapq:
            event = heapq.heappop(self.pq)[1]
            if not event.is_valid():
                continue
            a = event.a
            b = event.b

            for p in self.particles:
                p.move(event.time - self.t)
            
            self.t = event.time

            if a and b:
                a.bounce_off(b)
            elif a and not b:
                a.bounce_off_vertical_wall()
            elif not a and b:
                b.bounce_off_horizontal_wall()
            else:
                # yield self.particles
                self.redraw()
                heapq.heappush(self.pq, (self.t + 2, Event(self.t + 2, None, None)))
            self.predict(a)
            self.predict(b)
    
    def redraw(self):
        new_data = [(p.rx, p.ry) for p in self.particles]
        self.points.set_offsets(new_data)
        self.fig.canvas.draw_idle()
        # plt.pause(0.01)


def particles_to_coordinates(particles):
    p_count = len(particles)
    x = [None] * p_count
    y = [None] * p_count
    sizes = [None] * p_count
    for i, p in enumerate(particles):
        x[i] = p.rx
        y[i] = p.ry
        sizes[i] = 400 * p.radius
    return x, y, sizes


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Specify file path")
        sys.exit()
    file_path = sys.argv[1]
    with open(file_path) as fp:
        count_of_particles = int(fp.readline())
        particles = [None] * count_of_particles
        for i, line in enumerate(fp):
            line_content = line.split()
            particle = Particle(
                rx=float(line_content[0]),
                ry=float(line_content[1]),
                vx=float(line_content[2]),
                vy=float(line_content[3]),
                radius=float(line_content[4]),
                mass=float(line_content[5]),
            )
            particles[i] = particle

    system = CollisionSystem(particles)
    system.simulate()

