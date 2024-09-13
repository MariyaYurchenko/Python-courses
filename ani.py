import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation


def gen_vector(length, dims=2):
    helix = np.empty((dims, length))
    scale = 0.1
    for index in range(1, length):
        helix[:, index] = np.array([np.cos(4*np.pi*index/length),np.sin(4*np.pi*index/length),4*index/length])
        helix[:, index] = helix[:, index]*scale + np.array([0.5,0.5,0])

    return helix


def update_vector(num, dataLines, lines):
    for line, data in zip(lines, dataLines):
        line.set_data(data[0:2, :num])
        line.set_3d_properties(data[2, :num])
    return lines

fig = plt.figure()
ax = p3.Axes3D(fig)

data = [gen_vector(100, 3) for index in range(100)]

lines = [ax.plot(dat[0, 0:1], dat[1, 0:1], dat[2, 0:1])[0] for dat in data]

ax.set_xlim3d([0.0, 1.0])
ax.set_xlabel('X')

ax.set_ylim3d([0.0, 1.0])
ax.set_ylabel('Y')

ax.set_zlim3d([0.0, 1.0])
ax.set_zlabel('Z')

ax.set_title('Sensor data')

line_ani = animation.FuncAnimation(fig, update_vector, 100, fargs=(data, lines),
                                   interval=50, blit=False)

plt.show()
