# Generate random rewards for Condition and Treatment
import numpy as np
if self.action["treatment"] == "C":
    self.reward["value"] = np.random.normal(0, 1)
else:
    self.reward["value"] = np.random.normal(1, 1)
