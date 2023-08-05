from flask import * 
from collections import Counter
import time

app = Flask(__name__)  

def get_list():
    with open(r'.\text_file\words_alpha.txt', 'r') as f:
        rawText = f.read()

    word_list = [x.lower() for x in rawText.split('\n')]
    final = []
    for i in word_list:
        if len(i)>2:
            final.append(i)
    return final


def find_anagrams(letters):

    def is_anagram(word, letters_count):
        word_count = Counter(word)
        return all(word_count[c] <= letters_count[c] for c in word)

    word_list = get_list()
    letters_count = Counter(letters)
    anagrams = []

    for word in word_list:
        
        if is_anagram(word, letters_count):
            anagrams.append(word)

    return sorted(anagrams, key=lambda x: len(x))


def get_sol(word):
    solution_list = find_anagrams(word)
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
