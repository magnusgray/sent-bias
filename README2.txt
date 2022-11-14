Process Thus Far:

1. Clone github repository: 
Original: https://github.com/W4ngatang/sent-bias
Modified: https://github.com/kiromaru/sent-bias
Fork: https://github.com/magnusgray/sent-bias

2. Install conda: 
https://gist.github.com/kauffmanes/5e74916617f9993bc3479f401dfec7da

3. Set up conda environment:
conda env create -f environment.yml
source activate sentbias

4. More setup:
python -c 'import nltk; nltk.download("punkt")'
python -m spacy download en

5. Install glove: 
wget http://nlp.stanford.edu/data/glove.840B.300d.zip
unzip glove.840B.300d.zip

6. Install transformers:
conda install transformers

7. Obtain models:
git lfs install
git clone https://huggingface.co/dmis-lab/biobert-base-cased-v1.2
git clone https://huggingface.co/emilyalsentzer/Bio_ClinicalBERT
git clone https://huggingface.co/nlpaueb/legal-bert-base-uncased
git clone https://huggingface.co/microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext


8. Run code:
biobert ---> all good
python sentbias/main.py --log_file logs/biobert.log -t weat1,weat2,weat3,weat3b,weat4,weat5,weat5b,weat6,weat6b,weat7,weat7b,weat8,weat8b,weat9,weat10,sent-weat1,sent-weat2,sent-weat3,sent-weat3b,sent-weat4,sent-weat5,sent-weat5b,sent-weat6,sent-weat6b,sent-weat7,sent-weat7b,sent-weat8,sent-weat8b,sent-weat9,sent-weat10,angry_black_woman_stereotype,angry_black_woman_stereotype_b,sent-angry_black_woman_stereotype,sent-angry_black_woman_stereotype_b,heilman_double_bind_competent_1,heilman_double_bind_competent_1-,heilman_double_bind_competent_one_sentence,heilman_double_bind_competent_one_word,sent-heilman_double_bind_competent_one_word,heilman_double_bind_likable_1,heilman_double_bind_likable_1-,heilman_double_bind_likable_one_sentence,heilman_double_bind_likable_one_word,sent-heilman_double_bind_likable_one_word -m custom --model_path /home/magnusgray/projects/sent-bias/models/biobert-base-cased-v1.2 --exp_dir saves/biobert --data_dir tests/ --glove_path /home/magnusgray/projects/sent-bias/glove.840B.300d.txt -s 1111 --ignore_cached_encs

clinicalbert ---> this one does not work right now; version compatability issues 
python sentbias/main.py --log_file logs/clinicalbert.log -t weat1,weat2,weat3,weat3b,weat4,weat5,weat5b,weat6,weat6b,weat7,weat7b,weat8,weat8b,weat9,weat10,sent-weat1,sent-weat2,sent-weat3,sent-weat3b,sent-weat4,sent-weat5,sent-weat5b,sent-weat6,sent-weat6b,sent-weat7,sent-weat7b,sent-weat8,sent-weat8b,sent-weat9,sent-weat10,angry_black_woman_stereotype,angry_black_woman_stereotype_b,sent-angry_black_woman_stereotype,sent-angry_black_woman_stereotype_b,heilman_double_bind_competent_1,heilman_double_bind_competent_1-,heilman_double_bind_competent_one_sentence,heilman_double_bind_competent_one_word,sent-heilman_double_bind_competent_one_word,heilman_double_bind_likable_1,heilman_double_bind_likable_1-,heilman_double_bind_likable_one_sentence,heilman_double_bind_likable_one_word,sent-heilman_double_bind_likable_one_word -m custom --model_path /home/magnusgray/projects/sent-bias/models/Bio_ClinicalBERT --exp_dir saves/clinicalbert --data_dir tests/ --glove_path /home/magnusgray/projects/sent-bias/glove.840B.300d.txt -s 1111 --ignore_cached_encs

legalbert ---> all good
python sentbias/main.py --log_file logs/legalbert.log -t weat1,weat2,weat3,weat3b,weat4,weat5,weat5b,weat6,weat6b,weat7,weat7b,weat8,weat8b,weat9,weat10,sent-weat1,sent-weat2,sent-weat3,sent-weat3b,sent-weat4,sent-weat5,sent-weat5b,sent-weat6,sent-weat6b,sent-weat7,sent-weat7b,sent-weat8,sent-weat8b,sent-weat9,sent-weat10,angry_black_woman_stereotype,angry_black_woman_stereotype_b,sent-angry_black_woman_stereotype,sent-angry_black_woman_stereotype_b,heilman_double_bind_competent_1,heilman_double_bind_competent_1-,heilman_double_bind_competent_one_sentence,heilman_double_bind_competent_one_word,sent-heilman_double_bind_competent_one_word,heilman_double_bind_likable_1,heilman_double_bind_likable_1-,heilman_double_bind_likable_one_sentence,heilman_double_bind_likable_one_word,sent-heilman_double_bind_likable_one_word -m custom --model_path /home/magnusgray/projects/sent-bias/models/legal-bert-base-uncased --exp_dir saves/legalbert --data_dir tests/ --glove_path /home/magnusgray/projects/sent-bias/glove.840B.300d.txt -s 1111 --ignore_cached_encs

pubmedbert ---> this one does not work right now; version compatability issues
python sentbias/main.py --log_file logs/pubmedbert.log -t weat1,weat2,weat3,weat3b,weat4,weat5,weat5b,weat6,weat6b,weat7,weat7b,weat8,weat8b,weat9,weat10,sent-weat1,sent-weat2,sent-weat3,sent-weat3b,sent-weat4,sent-weat5,sent-weat5b,sent-weat6,sent-weat6b,sent-weat7,sent-weat7b,sent-weat8,sent-weat8b,sent-weat9,sent-weat10,angry_black_woman_stereotype,angry_black_woman_stereotype_b,sent-angry_black_woman_stereotype,sent-angry_black_woman_stereotype_b,heilman_double_bind_competent_1,heilman_double_bind_competent_1-,heilman_double_bind_competent_one_sentence,heilman_double_bind_competent_one_word,sent-heilman_double_bind_competent_one_word,heilman_double_bind_likable_1,heilman_double_bind_likable_1-,heilman_double_bind_likable_one_sentence,heilman_double_bind_likable_one_word,sent-heilman_double_bind_likable_one_word -m custom --model_path /home/magnusgray/projects/sent-bias/models/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext --exp_dir saves/pubmedbert --data_dir tests/ --glove_path /home/magnusgray/projects/sent-bias/glove.840B.300d.txt -s 1111 --ignore_cached_encs
