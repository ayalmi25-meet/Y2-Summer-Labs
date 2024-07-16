def create_youtube_video(title,description):
    create_new_video = {}
    create_new_video["title"] = title
    create_new_video["description"] = description
    create_new_video["likes"] = 0
    create_new_video["dislikes"] = 0
    create_new_video["comments"] = {}
    return create_new_video
	

def like(youtube_video={}):
	if "likes" in youtube_video:
		youtube_video["likes"]+=1

	return youtube_video


def dislike(youtube_video):
	if ("dislikes" in youtube_video):
		youtube_video["dislikes"]+=1

	return youtube_video


def add_comment(youtubevideo,username,comment_text):
	youtubevideo["comments"][username] = comment_text

	return youtubevideo




myvideo=create_youtube_video("fifa","playing fifa")
like(myvideo)
dislike(myvideo)
add_comment(myvideo,"ayal","liked it")

print(myvideo)

for i in range (495):




