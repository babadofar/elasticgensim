# Train word2vec models with gensim and elasticsearch
This project contains code to train gensim using data collected from an elasticsearch index. Attempts to train [word2vec](http://rare-technologies.com/word2vec-tutorial/). 


The loadwiki folder contains some scripts you can use to process a downloaded wiki file into an elasticsearc index. The script uses the Norwegian index located at https://dumps.wikimedia.org/other/cirrussearch/current/nowiki-20160822-cirrussearch-content.json.gz at the time of writing.
Needs a linux box or perhaps osx to run on. 

Vagrantfile included that will install a vm with ubuntu (install vagrant and virtualbox to use it, then issue `vagrant up` then `vagrant ssh; cd /vagrant`)

More info on the [elastic blog](https://www.elastic.co/blog/loading-wikipedia)