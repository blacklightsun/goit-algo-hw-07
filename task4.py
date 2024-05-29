class Comment:
    def __init__(self, comment, author):
        self.comment = comment
        self.author = author
        self.is_delete = False
        self.subcomments = []

    def add_reply(self, subcomment):
        self.subcomments.append(subcomment)
        return True

    def remove_reply(self):
        self.comment = 'Цей коментар було видалено.'
        self.is_delete = True
        return True

    def display(self, level=0):
        print('\t' * level + self.author + ': ' + self.comment + '\n' * 0)
        if bool(len(self.subcomments)):
            for subcomment in self.subcomments:
                subcomment.display(level + 1)


root_comment = Comment("Яка чудова книга!", "Бодя")

reply1 = Comment("Книга повне розчарування :(", "Андрій")
reply2 = Comment("Що в ній чудового?", "Марина")
root_comment.add_reply(reply1)
root_comment.add_reply(reply2)

reply1_1 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
reply1.add_reply(reply1_1)

print('\n' * 2 + 'Друк структури коментрів до видалення коментаря\n' + '-' * 50)
root_comment.display()

reply1.remove_reply()

print('\n' * 2 + 'Друк структури коментрів після видалення коментаря\n' + '-' * 50)
root_comment.display()

