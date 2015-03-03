import scipy.io.wavfile
import numpy as np
from scikits.talkbox.features import mfcc

def extract(input_path):
    sample_rate, X = scipy.io.wavfile.read(input_path)
    ceps, mspec, spec = mfcc(X)
    num_ceps = ceps.shape[0]
    features = np.mean(ceps[int(num_ceps*1/10):int(num_ceps*9/10)], axis=0)
    featuresVariance = np.var(ceps[int(num_ceps*1/10):int(num_ceps*9/10)], axis=0)

    return features


if __name__ == "__main__":
	print extract("./test.wav")