import h5py
from scipy.io import loadmat, savemat
import avalanchetoolbox
f = h5py.File(fname)

df = f['data'][:,:]

mat = loadmat(folder+'thresholds')

data = {}

print 'Local extrema event calculation'
extrema = ['local_extrema', 'excursion_extrema']
thresholds = ['SD1', 'SD2', 'SD3', 'SD4', 'Likelihood2', 'Likelihood5', 'Likelihood10', 'Likelihood20']

for ex in extrema:
    for thr in thresholds:
        print ex
        print thr
        data = {}
        e = avalanchetoolbox.avalanches.find_events(df,\
            thresholds_up=mat[thr+'_up'].flatten(), thresholds_down=mat[thr+'_down'].flatten(), event_detection=ex)
        data['event_times_'+thr+'_'+ex] = e['event_times']
        data['event_channels_'+thr+'_'+ex] = e['event_channels']

        savemat(folder+'events_'+thr+'_'+ex, data)
