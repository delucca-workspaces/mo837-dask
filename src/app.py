import time

from argparse import ArgumentParser
from dask import array as da
from dask.distributed import Client


def main(scheduler_url, size, chunk_size):
  if scheduler_url: launch_distributed_client(scheduler_url)

  print(f'Calculating the matrix multiplication of 2 ({size},{size}) matrices, divided into chunks of {chunk_size}')

  a = da.random.random((size, size), chunks=(chunk_size, chunk_size))
  b = da.random.random((size, size), chunks=(chunk_size, chunk_size))

  start_time = time.perf_counter()
  a.dot(b).compute()
  end_time = time.perf_counter()

  elapsed_time = end_time - start_time
  print('Compute time: {0:.2f} seconds'.format(elapsed_time))

def launch_distributed_client(scheduler_url):
  print(f'Using the scheduler located at: {scheduler_url}')
  client = Client(scheduler_url)


if __name__ == '__main__':
  parser = ArgumentParser(description='Matmul using Dask')
  parser.add_argument('--size', type=int, default=20000, help='the size of the matrix (default: 20000)')
  parser.add_argument('--chunk_size', type=int, default=10000, help='the size of the chunks (default: 10000)')
  parser.add_argument('--scheduler_url', type=str, help='the scheduler URL to be used')

  args = parser.parse_args()

  main(scheduler_url=args.scheduler_url, size=args.size, chunk_size=args.chunk_size)
