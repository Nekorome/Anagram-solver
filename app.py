from flask import * 
from itertools import permutations
import time

app = Flask(__name__)  

def get_list():
    with open('./text_file/words_alpha.txt', 'r') as f:
        dick = f.read()

    all = [x.lower() for x in dick.split('\n')]
    return(all)

def get_set():
    all = get_list()
    li = []

    for i in all:
        k = set(list(i))
        li.append(k)
    print("succesfully read the text file and created list")
    return(li,all)

def get_permutations(string):
    n = len(string)
    all_permutations = []

    for length in range(3, n + 1):
        perms = [''.join(p) for p in permutations(string, length)]
        all_permutations.extend(perms)

    return all_permutations

def find_val(string):

    word_list = get_permutations(string)

    se,li = get_set()
    probable_list = []
    for z in word_list:
        word = set(list(z))
        for i in range(len(se)):
            if se[i] == word:
                if len(z) == len(li[i]):
                    probable_list.append(li[i])

    return probable_list

def get_sol(word):
    solution_list = find_val(word)
    solution_list = list(set(solution_list))

    len_list = []
    for i in solution_list:
        len_list.append(len(i))

    len_list = list(set(len_list))
    
    dic = {}
    for i in len_list:
        arr = []

        for k in solution_list:
            if len(k) == i:
                arr.append(k)
            
        dic["word of length:"+str(i)] = arr

    return dic

@app.route('/')  
def renderPage():  
    return render_template('index.html') 

@app.route('/success', methods=['POST'])  
def success():  
    if request.method == 'POST':  

        search_values = request.form['values']
        if len(search_values) > 2:

            start_time = time.time()
            print(f"Request started on time: {start_time}")
            a = get_sol(search_values)
            end_time = time.time()
            
            print(f"Total time taken: {end_time-start_time}")
            
            return jsonify(text=a)
        else:
            return jsonify(text="You donkey")

if __name__ == '__main__':  
    app.run(host='0.0.0.0', debug=False)  
