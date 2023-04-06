import matplotlib.pyplot as plt
import numpy as np

def solve(theta,vi,target):
    g = 9.8
    tf = 2*vi*np.sin(theta)/g
    xf = vi*np.cos(theta)*tf
    return xf
# end

def MSE(theta,vi,target):
    xf = solve(theta,vi,target)
    return (xf-target)**2
# end

def Temp( i, T0, tau ):
    return T0*np.exp( -i/tau )
# end

def SA( start, nStep, pWidth, tau, vi, target ):
	
    points = [ start ]
    error  = [ MSE(start, vi, target) ]
    
    r = np.random.uniform(low=0, high=1, size=nStep)
    for step in range(nStep):
        print("step: " + str(step+1) + "/" + str(nStep))
        
        curr    = points[-1]
        currErr = error[-1]

        cand    = np.random.normal(curr,pWidth,size=1)[0]
        candErr = MSE(cand, vi, target)
        
        if( step == 0 ):
            T0 = abs(candErr - currErr)
        # end
        T = Temp( step, T0, tau )
        
        accProb = min( 1.0, np.exp( -(candErr-currErr)/T ) )
        
        if( r[step] <= accProb ):
            points.append(cand)
            error.append(candErr)
        else:
            points.append(curr)
            error.append(currErr)
        # end
	# end
    points = np.array(points)
    error  = np.array(error)
    
    return points, error

# end

nStep  = 1000
tau    = 400
pWidth = 0.2

start  = 45

vi     = 100
target = 500

points, error = SA( start, nStep, pWidth, tau, vi, target )

fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(5,15))

axes[0].plot(points)
axes[0].set_xlabel("step")
axes[0].set_ylabel("theta")

axes[1].plot(error)
axes[1].set_xlabel("step")
axes[1].set_ylabel("error")

xf = solve(points,vi,target)

axes[2].plot(xf)
axes[2].plot(target*np.ones_like(points),'r')
axes[2].set_xlabel("step")
axes[2].set_ylabel("xf")

