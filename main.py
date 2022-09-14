import random

count_down = 0
name = input('主人公の名前を決めてください >>')
print('{}さん、あなたはある日、船で仕事をしていた時見知らぬ島に流されてしまいました・・・!\n頑張れば10日でここを出られそう・・・\n頑張って脱出までにいろいろなことをしてください!'.format(name))
roop = 1
item = ['石ころ', '宝石', '珍しい石', '剣', '地図', '古文書', '名刺(名前:K.Y)', 'フィギュア(何かの)', '首輪', '錦鯉(こーんにーちわー...??)']
escape_success_or_failure = ['成功! 無事島に戻ることができた!', '失敗 途中で船が壊れてしまった・・・', 'また別の島に来てしまった・・・ 大変だ・・・']
animal = ['ウサギ', 'ネズミ', 'ドラゴ・・・ン??', 'パイソン', 'アナコンダ', '豚', '牛']
def main():
    print('朝です。')
    event = input('今日は何をしますか？ 1.探索 2.寝る 3.狩りをする 半角で入力してください。 >>')
    if event == '1':
        print('探索中・・・\n{}を見つけた!\nもう夕暮れだ!{}は眠りについた!'.format(random.choice(item), name))
        print('就寝中・・・\n')
    if event == '2':
        print('就寝中・・・\n')
    if event == '3':
        print('狩り中・・・\n{}を捕まえた!\mもう夕暮れだ!{}は眠りについた!'.format(random.choice(animal)))
        print('就寝中・・・\n')

while count_down < 10:
    count_down += 1
    main()

    if count_down == 10:
        print('脱出の出口を見つけた!')
        print('壊れた船があった!\n航海中・・・\n結果は・・・{}\nまた遊んでください!'.format(random.choice(escape_success_or_failure)))
