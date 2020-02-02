from myweb import db
from myweb import Post

db.create_all()
f = open("database", "r")

for line in f:
	line = line.rstrip('\n')
	list = line.split(': ')
	post = Post(author=list[0], category=list[1], content=list[2])
	db.session.add(post)
	db.session.commit()

posts = Post.query.all()
for p in posts:
	print(p.author)
	print(p.category)
	print(p.content)

