import functools
import statistics
import tracemalloc

def memory(func):

    @functools.wraps(func)
    def wraps(*args, **kwargs):
        tracemalloc.start()
        func(*args, **kwargs)
        snapshot = tracemalloc.take_snapshot()
        tracemalloc.stop()
        min_memory, max_memory = snapshot.statistics('Traceback')
        print("Total allocated size: %.1f MB" % (stat.size / 1024))
    return wraps
