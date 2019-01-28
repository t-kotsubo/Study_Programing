class A:
    
    def function(self):
        print('function_aを呼び出しました')
    
    def common(self):
        print('共有メソッドを呼び出しました')


class B(A):
    def function(self):
        super().function()
        print('function_bを呼び出しました')

class C(B):
    def function(self):
        print('function_cを呼び出しました')


# b = B()
# b.function()

c = C()
c.common()





