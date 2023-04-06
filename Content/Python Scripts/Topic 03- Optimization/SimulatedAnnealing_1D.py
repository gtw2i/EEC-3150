import matplotlib.pyplot as plt
import numpy as np

def f(x):
    #return x**2
    #return ( (x-1)**2+0.15 )*( (x+1)**2 )
    return np.abs(x) - np.cos(10*x)
# end

def Temp( t, T0, tau ):
    return T0*np.exp( -(1.0*t)/tau )
# end

def SA( start, nStep, pWidth, tau ):
	
    chain = [ start ]
    fit   = [ f(start) ]
    
    r = np.random.uniform(low=0, high=1, size=nStep)
    for step in range(nStep):
        print("step: " + str(step+1) + "/" + str(nStep))
        
        curr = chain[-1]
        currF = fit[-1]

        cand = np.random.normal(curr,pWidth,size=1)[0]
        candF = f( cand )
        
        if( step == 0 ):
            T0 = abs(candF - currF)
        # end
        T = Temp( step, T0, tau )
        
        accProb = min( 1.0, np.exp( -(candF-currF)/T ) )
        
        if( r[step] <= accProb ):
            chain.append(cand)
            fit.append(candF)
        else:
            chain.append(curr)
            fit.append(currF)
        # end
	# end
    chain = np.array(chain)
    fit   = np.array(fit)
    
    return chain, fit

# end


nStep  = 1000
tau    = 400
pWidth = 0.2
start  = 4

points, fit = SA( start, nStep, pWidth, tau )

xlim = max(max(abs(points)),start)

graphX = np.linspace(-xlim*1.15,xlim*1.15,100)

fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(5,15))

axes[0].plot(points,f(points),'b.',markersize=5)
axes[0].plot(points,f(points),'b',linewidth=1)
axes[0].plot(graphX,f(graphX),'r')
axes[0].set_xlabel("x")
axes[0].set_ylabel("f(x)")

axes[1].plot(points)
axes[1].set_ylim(-xlim,xlim)
axes[1].set_xlabel("step")
axes[1].set_ylabel("x")

axes[2].plot(fit)
# axes[2].set_ylim(0,max(fit))
axes[2].set_xlabel("step")
axes[2].set_ylabel("f(x)")
