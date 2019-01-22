class Hero():
    def __init__(self, name, hp):
        self.name = name # 通常のメンバ変数

        self.__hp = hp # プライベート変数

    def self_introduction(self):
        print("私の名前は勇者%sです。" % (self.__name))

    def get_hp(self): # ゲッター
        return self.__hp

    def set_hp(self, new_hp): # セッター
        self.__hp = new_hp

hero = Hero("ヨシヒコ", 10)
print(hero.name)
print(hero.get_hp())
hero.set_hp(15)
print(hero.get_hp())
