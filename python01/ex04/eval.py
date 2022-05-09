class Evaluator:
    def zip_evaluate(coefs, values):
        ret = 0
        if (type(values) == list and type(coefs) == list
           and len(values) == len(coefs)):
            for i, s in zip(coefs, values):
                ret += i * len(s)
            return ret
        else:
            return -1

    def enumerate_evaluate(coefs, values):
        ret = 0
        if (type(values) == list and type(coefs) == list
           and len(values) == len(coefs)):
            for i, s in enumerate(values):
                ret += len(s) * coefs[i]
            return ret
        else:
            return -1
