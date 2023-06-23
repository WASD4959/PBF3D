# PBF3D

This repository is the implementation of PBF (Postion Based Fluid)  based on taichi, and with help of particle2obj tool in [fluid-engine-dev](https://github.com/doyubkim/fluid-engine-dev) to make particles to mesh, finally use blender to render animation.

## Dependencies

```
taichi			(tested with 1.5.0)
opencv-python	(tested with 4.5.5)

blender			(tested with blender 3.6.0-usd.200.0)
```

## Overall process

1. first run pbf3d.py to get particles' position and save to local (the file extension should be xyz);
2. run particle2obj.py to generate mesh per frame (you can adjust the kernel_size as needed);
3. run animate.py in blender, this is a blender script to import mesh and generate animation;
4. use blender to render each frame of the image and save local;
5. run pic2vedio.py to make images to vedio;

## Result 

![PBF3D.gif](https://github.com/WASD4959/PBF3D/blob/master/res/PBF3D.gif?raw=true)

![res_01.gif](https://github.com/WASD4959/PBF3D/blob/master/res/res_01.gif?raw=true)

![res_02.gif](https://github.com/WASD4959/PBF3D/blob/master/res/res_02.gif?raw=true)

## References

paper: [Macklin, M., Müller, M. 2013. Position Based Fluids. ACM Trans. Graph. 32, 4, Article 104, July 2013, 5 pages](http://doi.acm.org/10.1145/2461912.2461984)

https://github.com/chunleili/pbf3d

https://github.com/doyubkim/fluid-engine-dev
