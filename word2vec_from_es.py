

import gensim, logging, nltk
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
from nltk.corpus import stopwords

class MySentences(object):

    def __init__(self):
      # Initialize the scroll
          page = es.search(
            index = 'indexname',
            doc_type = 'product',
            scroll = '2m',
            search_type = 'scan',
            size = 1000,
            body = {
              # Your query's body (optional)
              })
          self.sid = page['_scroll_id']
          self.scroll_size = page['hits']['total']
          self.iterations = 10
          self.iter = 0
          self.stop = set(stopwords.words('norwegian'))

    def __iter__(self):
         while (self.scroll_size > 0 and self.iter < self.iterations):
              self.iter += 1
              print "Scrolling..."
              page = es.scroll(scroll_id = self.sid, scroll = '2m')
              # Update the scroll ID
              self.sid = page['_scroll_id']
              # Get the number of results that we returned in the last scroll
              self.scroll_size = len(page['hits']['hits'])

              print "scroll size: " + str(self.scroll_size)
              # Do something with the obtained page
              for hit in page['hits']['hits']:
                    text = []
                    # add the fields you need in this
                    text.append (hit['_source']['name'])
                    if 'description' in hit['_source']:
                        text.append(hit['_source']['description'])
                    for item in text:
                        item = item.replace(',', ' ').replace('(', '').replace(')', '').lower().split()
                        item2 = []
                        for word in item:
                            if word not in self.stop:
                                item2.append(word)

                        print item2
                        yield item2

from elasticsearch import Elasticsearch
import re
es =  Elasticsearch('localhost:9200')

sentences = MySentences()
model = gensim.models.Word2Vec(sentences, min_count=2)

model
model.save('model.mod')
model.save_word2vec_format('model.txt', binary=False)
#print model.most_similar('opprinnelig')

print model.most_similar('kaffe')

  
 