class Student:
    
    def __init__(self,name): #コンストラクタ　初期化
        self.name = name     #アトリビュート

    def avg(self,math,english): #メソッド
        print((math + english)/2)

a001 = Student("sato") #インスタンス化 オブジェクト生成
a002 = Student("tanaka") #a002=インスタンス Student クラス

print(a001.name)
print(a002.name)
