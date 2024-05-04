import os 
try :
    from flask import Flask ,render_template ,request ,redirect
except :
    os.system('pip install flask')
    from flask import Flask ,render_template ,request ,redirect
try :
    from PIL import Image
except :
    os.system('pip install Pillow')
    from PIL import Image

def refresh():
    os.system('sleep .3')
    os.system('adb shell screencap -p /sdcard/screen.png')
    os.system('adb pull /sdcard/screen.png ./')

def keyevent(integer):
    os.system('adb shell input keyevent '+str(integer))
    refresh()

def get_image_size():
    with Image.open('screen.png') as img:
        width, height = img.size
        return height,width


app=Flask(__name__)
@app.route('/') 
def index():
    return render_template('index.html',size=get_image_size())


@app.route('/submit', methods=['GET'])
def submit():
    text = request.args.get('text')
    os.system('adb disconnect ')
    os.system('adb connect '+text)
    refresh()
    return redirect('/')

@app.route('/clicked', methods=['GET'])
def clicked():
    x = request.args.get('x')
    y = request.args.get('y')
    os.system('adb shell input tap '+str(x)+' '+str(y))
    refresh()
    return redirect('/')

@app.route('/text', methods=['GET'])
def text():
    text = request.args.get('text')
    os.system(f'adb shell input text "{text}"')
    refresh()
    return redirect('/')



@app.route('/pressed', methods=['GET'])
def button():
    text = request.args.get('btn')

    if text =='refresh' :
        refresh()
    elif text =='left':
        keyevent(21)    
    elif text =='up':
        keyevent(19)    
    elif text =='down':
        keyevent(20)    
    elif text =='right':
        keyevent(22)    
    elif text =='enter':
        keyevent(66) 
    elif text == 'power_on_off':
        keyevent(26)
    elif text == 'backspace':
        keyevent(67)
    elif text == 'home':
        keyevent(3)
    elif text =='recent':
        keyevent(187)
    return redirect('/')
app.run(host='0.0.0.0',debug=False)