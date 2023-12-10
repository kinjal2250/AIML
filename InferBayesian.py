# Example: Harry installed a new burglar alarm at his home to detect burglary. The alarm reliably responds at detecting a burglary but also responds for minor earthquakes. Harry has two neighbors David and Sophia, who have taken a responsibility to inform Harry at work when they hear the alarm. David always calls Harry when he hears the alarm, but sometimes he got confused with the phone ringing and calls at that time too. On the other hand, Sophia likes to listen to high music, so sometimes she misses to hear the alarm. Here we would like to compute the probability of Burglary Alarm.
from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
# Burglary --> Alarm --> DavidCalls
#          \        /
#           \      /
#            Earthquake
#              |
#          SophiaCalls
# Define the structure of the Bayesian network
model = BayesianNetwork([('Burglary', 'Alarm'), ('Earthquake', 'Alarm'),
                         ('Alarm', 'DavidCalls'), ('Alarm', 'SophiaCalls')])
# Define CPDs for the Burglary variable
cpd_burglary = TabularCPD(variable='Burglary', variable_card=2, values=[[0.001], [0.999]])

# Define CPDs for the Earthquake variable
cpd_earthquake = TabularCPD(variable='Earthquake', variable_card=2, values=[[0.002], [0.998]])

# Define CPD for the Alarm variable
cpd_alarm = TabularCPD(variable='Alarm', variable_card=2,
                       values=[[0.95, 0.94, 0.29, 0.001],
                               [0.05, 0.06, 0.71, 0.999]],
                       evidence=['Burglary', 'Earthquake'], evidence_card=[2, 2])

# Define CPDs for DavidCalls and SophiaCalls
cpd_david_calls = TabularCPD(variable='DavidCalls', variable_card=2,
                             values=[[0.1, 0.6], [0.9, 0.4]],
                             evidence=['Alarm'], evidence_card=[2])

cpd_sophia_calls = TabularCPD(variable='SophiaCalls', variable_card=2,
                              values=[[0.3, 0.8], [0.7, 0.2]],
                              evidence=['Alarm'], evidence_card=[2])
# Add the CPDs to the Bayesian network
model.add_cpds(cpd_burglary, cpd_earthquake, cpd_alarm, cpd_david_calls, cpd_sophia_calls)
# Verify the network structure and CPDs
assert model.check_model()
# Initialize the Variable Elimination algorithm for inference
inference = VariableElimination(model)
# Compute the probability of the Burglary Alarm given the evidence
result = inference.query(variables=['Alarm'], evidence=None)
print(result)

