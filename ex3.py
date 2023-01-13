class Aggregator:

    def __init__(self, agg_type: type, ignore_errors: bool = True):

        self.agg_type = agg_type
        self.ignore_errors = ignore_errors
        self.agg = None

    def __call__(self, *args):
        for arg in args:
            if not isinstance(arg, self.agg_type):
                if not self.ignore_errors:
                    raise TypeError(f"aggregation only works on type 'str', not 'int")
            elif self.agg is None:
                self.agg = arg
            else:
                self.agg =self.agg+ arg

        return self.agg

int_agg = Aggregator(agg_type=int)
int_agg(1, 2, 3)
int_agg(4, "hi", 5.1)
print(int_agg())
str_agg = Aggregator(agg_type=str, ignore_errors=False)
print(str_agg("this", " ", "is a test"))
try:
    str_agg(1)
except TypeError as e:
    print(f"{type(e).__name__}: {e}")
