import hpccm

# Base
Stage0 += baseimage(image='ubuntu')

# Dask Distributed
Stage0 += pip(packages=['numpy', 'pandas', 'dask', 'distributed'], pip='pip3')
