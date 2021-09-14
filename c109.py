import pandas as pd
import csv
import statistics

df = pd.read_csv('height-weight.csv')
heightlist = df ['Height(Inches)'].tolist()
weightlist = df ['Weight(Pounds)'].tolist()

heightmean=statistics.mean(heightlist)
weightmean=statistics.mean(weightlist)

heightmedian=statistics.median(heightlist)
weightmedian=statistics.median(weightlist)

heightmode=statistics.mode(heightlist)
weightmode=statistics.mode(weightlist)

heightstd=statistics.stdev(heightlist)
weightstd=statistics.stdev(weightlist)

print('mean,meadian,mode,stdev for hight are',heightmean,heightmedian,heightmode,heightstd)
print('mean,meadian,mode,stdev for weight are',weightmean,weightmedian,weightmode,weightstd)

height_first_std_start,height_first_std_end = heightmean - heightstd, heightmean + heightstd
height_second_std_start,height_second_std_end = heightmean - heightstd*2, heightmean + heightstd*2
height_third_std_start,height_third_std_end = heightmean - heightstd*3, heightmean + heightstd*3
heightlistofdatawithinfirststd = [result for result in heightlist if result > height_first_std_start and result < height_first_std_end]
heightlistofdatawithinsecondstd = [result for result in heightlist if result > height_second_std_start and result < height_second_std_end]
heightlistofdatawithinthirdstd = [result for result in heightlist if result > height_third_std_start and result < height_third_std_end]
print('{} % of data for height lies within first std range'.format(len(heightlistofdatawithinfirststd)*100.0/len(heightlist)))
print('{} % of data for height lies within second std range'.format(len(heightlistofdatawithinsecondstd)*100.0/len(heightlist)))
print('{} % of data for height lies within third std range'.format(len(heightlistofdatawithinthirdstd)*100.0/len(heightlist)))

weight_first_std_start,weight_first_std_end = weightmean - weightstd, weightmean + weightstd
weight_second_std_start,weight_second_std_end = weightmean - weightstd*2, weightmean + weightstd*2
weight_third_std_start,weight_third_std_end = weightmean - weightstd*3, weightmean + weightstd*3
weightlistofdatawithinfirststd = [result for result in weightlist if result > weight_first_std_start and result < weight_first_std_end]
weightlistofdatawithinsecondstd = [result for result in weightlist if result > weight_second_std_start and result < weight_second_std_end]
weightlistofdatawithinthirdstd = [result for result in weightlist if result > weight_third_std_start and result < weight_third_std_end]
print('{} % of data for weight lies within first std range'.format(len(weightlistofdatawithinfirststd)*100.0/len(weightlist)))
print('{} % of data for weight lies within second std range'.format(len(weightlistofdatawithinsecondstd)*100.0/len(weightlist)))
print('{} % of data for weight lies within third std range'.format(len(weightlistofdatawithinthirdstd)*100.0/len(weightlist)))