import h5py
import dask.array as da

from blaze import data, into

f = h5py.File('myfile.hdf5', 'a')
A = f.create_dataset(name='A', shape=(200000, 4000), dtype='f8',
                     chunks=(250, 250), fillvalue=1.0)
B = f.create_dataset(name='B', shape=(4000, 4000), dtype='f8',
                     chunks=(250, 250), fillvalue=1.0)

a = into(da.from_array(), 'myfile.hdf5::/A', blockshape=(1000, 1000))
b = into(da.from_array(), 'myfile.hdf5::/B', blockshape=(1000, 1000))
A = data(a)
B = data(b)

into('myfile.hdf5::/result', A.dot(B))
