from flask import Flask

app = Flask(__name__)



@app.route('/home')
def home():
    return("<html><h1>HEYY</h1><p>welcome to a photo gallery containing three types of photos: food, pets, and outer space. have fun</p><a href = '/food1'>go to the first pood photo</a><a href = '/pet2'>go to the second pet photo</a><a href = '/space1'>go to the first space photo</a></html>")
  
@app.route('/food1')
def food1():
    return("<html><h1>FIRST FOOD PHOTO:</h1><img src='https://t1.gstatic.com/licensed-image?q=tbn:ANd9GcRoeUqD7lgiXavof_C8DW2QeI-BHIzGPLKRPCWinurLGGMBT7GSml0le6bQro8yWjAa'><p>pizza!!</p><a href = '/home'>HOME</a><a href='food2'>MORE FOOD PHOTOS</a></html>")


@app.route('/food2')
def food2():
    return("<html><h1>SECOND FOOD PHOTO:</h1><img src='https://www.allrecipes.com/thmb/QiGptPjQB5mqSXGVxE4sLPMJs_4=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/AR-269500-creamy-garlic-pasta-Beauties-2x1-bcd9cb83138849e4b17104a1cd51d063.jpg'><p>pasta!!!!</p><a href = '/food1'>HOME</a><a href='food3'>MORE FOOD PHOTOS</a></html>")



@app.route('/food3')
def food3():
    return("<html><h1>THIRD FOOD PHOTO:</h1><img src='https://www.foodandwine.com/thmb/pwFie7NRkq4SXMDJU6QKnUKlaoI=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/Ultimate-Veggie-Burgers-FT-Recipe-0821-5d7532c53a924a7298d2175cf1d4219f.jpg'><p>burger!!!!</p><a href = '/home'>HOME</a><a href='/food2'>MORE FOOD PHOTOS</a></html>")



@app.route('/pet2')
def pet2():
    return("<html><h1> FIRST PET PHOTO:</h1><img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSArtNvfXmXPL3m2NUPQYsze8TP_rJpeYMTxA&s'><p>dogii!!!!</p><a href='/pet3'>want more?</a><a href='/pet1'>MORE PET PHOTOS</a><a href='/home'>HOME</a></html>")



@app.route('/pet1')
def pet1():
    return("<html><h1>SECOND PET PHOTO:</h1><img src='https://cdn.britannica.com/79/232779-050-6B0411D7/German-Shepherd-dog-Alsatian.jpg'><p>dog!!!!</p><a href='/pet2'>more pet?</a></html>")



@app.route('/pet3')
def pet3():
    return("<html><h1>THIRD PET PHOTO:</h1><img src='https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Cat_August_2010-4.jpg/1200px-Cat_August_2010-4.jpg'><p>cat!!!!</p><a href = '/pet2'>more pet</a></html>")



@app.route('/space1')
def space1():
    return("<html><h1>FIRST SPACE PHOTO:</h1><img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSE8rlBbqnDycGlg4HYo7CnnMOdSE7JA6ICkg&s'><p>beutifull!!!!</p><a href = '/home'>HOME</a><a href='/space3'>MORE SPACE PHOTOS</a><a href='/space2'>MORE SPACE PHOTOS</a></html>")



@app.route('/space2')
def space2():
    return("<html><h1>SECOND SPACE PHOTO:</h1><img src='https://prd-sc102-cdn.rtx.com/-/media/ca/product-assets/marketing/s/space/space-symposium-graphic_1920x1080.jpg?rev=2a22f490c9c644a5bf69ef3cce59813d'><p>space woww!!!!</p><a href = '/space1'>more space</a><a href='space3'>AND MORE</a></html>")



@app.route('/space3')
def space3():
    return("<html><h1>THIRD SPACE PHOTO:</h1><img src='https://t4.ftcdn.net/jpg/03/86/82/73/360_F_386827376_uWOOhKGk6A4UVL5imUBt20Bh8cmODqzx.jpg'><p>crazy!!!!</p><a href = '/space2'>MOREEE</a><a href='space1'>AND MORE</a></html>")








if __name__ == '__main__':
    app.run(debug=True)




