data_path = '/data/alstottj/Culture/'

import MCS
import avalanchetoolbox
import h5py
import os
from scipy.io import loadmat
from numpy import array

dirlist = os.listdir(data_path)

for i in dirlist:
    if i[-4:]=='.raw':
        print i
        file = data_path+i
        d, sampling_rate, electrode_names = MCS.raw_import(file)

        print 'Filtering'
        df, frequencies, sampling_rate = avalanchetoolbox.preprocessing.band_filter(d, 'broad', sampling_rate, downsample=1000.0)

        fname = file[:-4]+'.h5'
        data = h5py.File(fname)
        data['data'] = df

        badelec_mat = loadmat(file[:-4]+'badelec.mat')
        badelec = badelec_mat['badelec']

        if not badelec.any():
            badelec = array([0])

        data['badelec'] = badelec

        print 'SD calculation'
        data['SD1_up'], data['SD1_down'] = avalanchetoolbox.avalanches.find_thresholds(df, 'SD', 1, 'both')
        data['SD2_up'], data['SD2_down'] = avalanchetoolbox.avalanches.find_thresholds(df, 'SD', 2, 'both')
        data['SD3_up'], data['SD3_down'] = avalanchetoolbox.avalanches.find_thresholds(df, 'SD', 3, 'both')
        data['SD4_up'], data['SD4_down'] = avalanchetoolbox.avalanches.find_thresholds(df, 'SD', 4, 'both')

        print 'Likelihood calculation'
        print '2'
        data['Likelihood2_up'], data['Likelihood2_down'] = avalanchetoolbox.avalanches.find_thresholds(df, 'Likelihood', 2, 'both')
        print '5'
        data['Likelihood5_up'], data['Likelihood5_down'] = avalanchetoolbox.avalanches.find_thresholds(df, 'Likelihood', 5, 'both')
        print '10'
        data['Likelihood10_up'], data['Likelihood10_down'] = avalanchetoolbox.avalanches.find_thresholds(df, 'Likelihood', 10, 'both')
        print '20'
        data['Likelihood20_up'], data['Likelihood20_down'] = avalanchetoolbox.avalanches.find_thresholds(df, 'Likelihood', 20, 'both')

        print 'Local extrema event calculation'
        data['event_times_SD1_local_extrema'], data['event_channels_SD1_local_extrema'], iei = avalanchetoolbox.find_events(df,\
                thresholds_up=data['SD1_up'], thresholds_down=['SD1_down'], event_detection='local_extrema')
        data['event_times_SD2_local_extrema'], data['event_channels_SD2_local_extrema'], iei = avalanchetoolbox.find_events(df,\
                thresholds_up=data['SD2_up'], thresholds_down=['SD2_down'], event_detection='local_extrema')
        data['event_times_SD3_local_extrema'], data['event_channels_SD3_local_extrema'], iei = avalanchetoolbox.find_events(df,\
                thresholds_up=data['SD3_up'], thresholds_down=['SD3_down'], event_detection='local_extrema')
        data['event_times_SD4_local_extrema'], data['event_channels_SD4_local_extrema'], iei = avalanchetoolbox.find_events(df,\
                thresholds_up=data['SD4_up'], thresholds_down=['SD4_down'], event_detection='local_extrema')

        data['event_times_Likelihood2_local_extrema'], data['event_channels_Likelihood2_local_extrema'], iei = avalanchetoolbox.find_events(df,\
                thresholds_up=data['Likelihood2_up'], thresholds_down=['Likelihood2_down'], event_detection='local_extrema')
        data['event_times_Likelihood5_local_extrema'], data['event_channels_Likelihood5_local_extrema'], iei = avalanchetoolbox.find_events(df,\
                thresholds_up=data['Likelihood5_up'], thresholds_down=['Likelihood5_down'], event_detection='local_extrema')
        data['event_times_Likelihood10_local_extrema'], data['event_channels_Likelihood10_local_extrema'], iei = avalanchetoolbox.find_events(df,\
                thresholds_up=data['Likelihood10_up'], thresholds_down=['Likelihood10_down'], event_detection='local_extrema')
        data['event_times_Likelihood20_local_extrema'], data['event_channels_Likelihood20_local_extrema'], iei = avalanchetoolbox.find_events(df,\
                thresholds_up=data['Likelihood20_up'], thresholds_down=['Likelihood20_down'], event_detection='local_extrema')

        print 'Excursion extrema event calculation'
        data['event_times_SD1_excursion_extrema'], data['event_channels_SD1_excursion_extrema'], iei = avalanchetoolbox.find_events(df,\
                thresholds_up=data['SD1_up'], thresholds_down=['SD1_down'], event_detection='excursion_extrema')
        data['event_times_SD2_excursion_extrema'], data['event_channels_SD2_excursion_extrema'], iei = avalanchetoolbox.find_events(df,\
                thresholds_up=data['SD2_up'], thresholds_down=['SD2_down'], event_detection='excursion_extrema')
        data['event_times_SD3_excursion_extrema'], data['event_channels_SD3_excursion_extrema'], iei = avalanchetoolbox.find_events(df,\
                thresholds_up=data['SD3_up'], thresholds_down=['SD3_down'], event_detection='excursion_extrema')
        data['event_times_SD4_excursion_extrema'], data['event_channels_SD4_excursion_extrema'], iei = avalanchetoolbox.find_events(df,\
                thresholds_up=data['SD4_up'], thresholds_down=['SD4_down'], event_detection='excursion_extrema')

        data['event_times_Likelihood2_excursion_extrema'], data['event_channels_Likelihood2_excursion_extrema'], iei = avalanchetoolbox.find_events(df,\
                thresholds_up=data['Likelihood2_up'], thresholds_down=['Likelihood2_down'], event_detection='excursion_extrema')
        data['event_times_Likelihood5_excursion_extrema'], data['event_channels_Likelihood5_excursion_extrema'], iei = avalanchetoolbox.find_events(df,\
                thresholds_up=data['Likelihood5_up'], thresholds_down=['Likelihood5_down'], event_detection='excursion_extrema')
        data['event_times_Likelihood10_excursion_extrema'], data['event_channels_Likelihood10_excursion_extrema'], iei = avalanchetoolbox.find_events(df,\
                thresholds_up=data['Likelihood10_up'], thresholds_down=['Likelihood10_down'], event_detection='excursion_extrema')
        data['event_times_Likelihood20_excursion_extrema'], data['event_channels_Likelihood20_excursion_extrema'], iei = avalanchetoolbox.find_events(df,\
                thresholds_up=data['Likelihood20_up'], thresholds_down=['Likelihood20_down'], event_detection='excursion_extrema')

        data.close()
