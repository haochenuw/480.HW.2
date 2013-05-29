︠d7e35277-7ce6-4b4e-b287-2624bebf9f61︠
#hidden markov model for my evening

A = matrix(RR, 4, [.50, .50, 0,  0,  # hungry
                   .0, .55, .45, 0,  # eat
                    0,   0, .95, .05, # full(can't do anything)
                   .40,   0,   0, .60]) # study

emission_symbols = ['so hungry', 'cooking', 'eating', 'so full', 'Oh yeah!', 'feel bad']
B = matrix(RR, 4, 6, [.3,.4,0,0,0,.3,  # hungry
                      0,0,.5,0,.5,0,  # eating
                      0,0,0,0.4,0.3,0.3, # full
                      0.2,0,0,0,0.5,0.3]) #study

initial = [1,0,0,0]

model = hmm.DiscreteHiddenMarkovModel(A, B, initial, emission_symbols)
50
︡f97a8203-87de-48bd-86a2-5f1eba35a18a︡{"stdout":"50\n"}︡
︠280df5ad-ed9e-4ded-aeb2-63f41fca8f28︠
model
︡c068390b-22df-49bb-8942-987c8944ed06︡{"stdout":"Discrete Hidden Markov Model with 4 States and 6 Emissions\nTransition matrix:\n[ 0.5  0.5  0.0  0.0]\n[ 0.0 0.55 0.45  0.0]\n[ 0.0  0.0 0.95 0.05]\n[ 0.4  0.0  0.0  0.6]\nEmission matrix:\n[0.3 0.4 0.0 0.0 0.0 0.3]\n[0.0 0.0 0.5 0.0 0.5 0.0]\n[0.0 0.0 0.0 0.4 0.3 0.3]\n[0.2 0.0 0.0 0.0 0.5 0.3]\nInitial probabilities: [1.0000, 0.0000, 0.0000, 0.0000]\nEmission symbols: ['so hungry', 'cooking', 'eating', 'so full', 'Oh yeah!', 'feel bad']\n"}︡
︠c9b38f86-1aa3-4853-85f5-f65cdb72d499︠
model.graph().plot(edge_labels=True, graph_border=True).show(figsize=5, svg=True)
︡eded6df4-18eb-4418-b26c-4a9dcf74a3fb︡{"file":{"show":true,"uuid":"05c4b807-6ef1-409c-a702-a439bf761520","filename":"/mnt/home/5exnPEXb/.sage/temp/compute2a/21118/tmp_6A8TtO.svg"}}︡
︠40efd2a0-e906-46f2-9f42-81cf6c75dfcf︠
set_random_seed(0); model.sample(20)
︡402d7c50-6de6-4ba0-b59d-ae8a0bac996b︡{"stdout":"['so hungry', 'so hungry', 'eating', 'eating', 'eating', 'Oh yeah!', 'eating', 'eating', 'eating', 'Oh yeah!', 'Oh yeah!', 'feel bad', 'Oh yeah!', 'so full', 'so full', 'Oh yeah!', 'so full', 'feel bad', 'so full', 'Oh yeah!']\n"}︡
︠237b44de-dc07-444f-b388-1796ade20361︠
