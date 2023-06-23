#Turn Particles to Mesh

import subprocess
import os

xyz_path = './data/01/xyz'
obj_path = './data/01/obj'

#run particles2obj.exe to generate obj
def gen_obj(p2obj,input,output,kernel_size):
    result = subprocess.run([p2obj, '-i', input, '-o', output, '-k', kernel_size], capture_output=True)
    print(result.stdout)

if __name__ == '__main__':
    p2obj = 'particles2obj.exe'
    kernel_size = '0.02'
    for i in range(300,600):
        filename = 'Frame_'+ str(i) + '.xyz'
        outfile = 'Frame_' + str(i) + '.obj'
        input = os.path.join(xyz_path,filename)
        output = os.path.join(obj_path, outfile)
        #print(output)
        #kernel_size effects the precision of the model
        gen_obj(p2obj,input,output,kernel_size)
