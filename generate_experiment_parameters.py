import itertools
import json

exp_params = {
    'max_learning_rate': [0.4, 0.6],
    'data_aug_cutout_size': [5, 12],
    'batch_size': [128, 256],
    'momentum': [0.9, 0.99],
    'batch_norm': ['true'],
    'epochs': [10]
}

keys, values = zip(*exp_params.items())
# exp_params_allsets = [dict(exp_param_set=dict(zip(keys, v))) for v in itertools.product(*values)]
exp_params_allsets = [dict(zip(keys, v)) for v in itertools.product(*values)]

with open('experiment_set.json', 'w') as outfile:
    json.dump(exp_params_allsets, outfile)

print("Total number of experiment parameters sets: "+str(len(exp_params_allsets)))
print("Experiment sets saved to: "+'exp_params_allsets.json')


