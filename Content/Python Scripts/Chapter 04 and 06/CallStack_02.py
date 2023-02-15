def f():
    def g():
        return 1+'c'
    # end
    g()
# end

f()