import re

ml_text = ['/home/sivakumar/2020_fall_hackathon_project/bert_summarizer/data_processing/machine_learning/classification.txt',
           '/home/sivakumar/2020_fall_hackathon_project/bert_summarizer/data_processing/machine_learning/clustering.txt',
           '/home/sivakumar/2020_fall_hackathon_project/bert_summarizer/data_processing/machine_learning/dimensionality_reduction.txt',
           '/home/sivakumar/2020_fall_hackathon_project/bert_summarizer/data_processing/machine_learning/regression.txt',
           '/home/sivakumar/2020_fall_hackathon_project/bert_summarizer/data_processing/machine_learning/supervised_learning.txt']

network_text = ['/home/sivakumar/2020_fall_hackathon_project/bert_summarizer/data_processing/networks/basics.txt',
                '/home/sivakumar/2020_fall_hackathon_project/bert_summarizer/data_processing/networks/data_link_layer.txt',
                '/home/sivakumar/2020_fall_hackathon_project/bert_summarizer/data_processing/networks/network_layer.txt',
                '/home/sivakumar/2020_fall_hackathon_project/bert_summarizer/data_processing/networks/physical_Layer.txt']

for file in ml_text:
    with open(file, 'r') as f:
        text = f.read()
        f.close()
    with open(file, 'w') as f:
        print('pre-processing the file {}'.format(file))
        text = re.sub("[!@#$+%*:()'-]", ' ', text)
        text = text.lower()
        f.write(text)
        f.close()

for file in network_text:
    with open(file, 'r') as f:
        text = f.read()
        f.close()
    with open(file, 'w') as f:
        print('pre-processing the file {}'.format(file))
        text = re.sub("[!@#$+%*:()'-]", ' ', text)
        text = text.lower()
        f.write(text)
        f.close()

