# -*- coding: utf-8 -*-
"""
This simple program creates a dictionary class to allow user to extract the definition of a word

"""
import json

class Dictionary:
    
    def __init__(self, path = './english_dict.json'):
        
        self.data = self.load_data(path)
    
    def load_data(self, path):
        """Loads the json file of words with definitions"""

        with open (path) as f:
            data = json.load(f)
        
        return data
    
    def get_query(self):
        """Asks user which word to define"""
        
        query = input("What word would you like to define? ")
        
        return query
    
    def lookup_definition(self):
        """Prints the definition"""
        
        while True:
            query = self.get_query()
            
            if query in self.data.keys():
                definition = self.data[query]
                print(f"\n {query} means: {definition}")

            else:
                print(f"{query} not in dictionary")
            
            
