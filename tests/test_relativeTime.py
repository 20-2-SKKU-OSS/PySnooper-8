mport pysnooper

def g():
        yield 8

@pysnooper.snoop(relative_time=True)
    def f():
        yield from g()

tuple(f())
