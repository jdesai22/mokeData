import matplotlib.pyplot as plt
from scipy.signal import savgol_filter

def main():
    path = str(input("Path to Data File: "))
    scans = int(input("Scans from 0 to Max Voltage: "))
    loops = int(input("Loops: "))
    run = str(input("Ready to Run?(y/n) "))

    scansPerLoop = 1 + (scans * 4)

    while run == "y":

        voltages = []
        allVoltages = []
        averagePhotodiodes = []
        allPhotodiode = []
        photodiode = []

        with open(path, 'r') as file:
            splitFile = file.read().split()

            count = 0

            for i in range(0, len(splitFile)):
                if (splitFile[i] == "X_Value,Untitled,Comment"):
                    allVoltages.append((float) (splitFile[i + 1].replace(',', '')))
                    allPhotodiode.append((float) (splitFile[i + 2].replace(',', '')))

            # totalLoops = ( scans * 4 +1)  * loops
            voltages = allVoltages[0:scansPerLoop]

            for i in range(0, loops):
                photodiode.append(allPhotodiode[i * scansPerLoop : (i + 1) * scansPerLoop])


            reshapePhotodiode = []
            # #
            for i in range(0, len(photodiode[0])):
                inter = []
                for s in range(0, len(photodiode)):
                    try:
                        inter.append(photodiode[s][i])
                    except IndexError:
                        continue
                reshapePhotodiode.append(inter)

            # #
            for i in reshapePhotodiode:
                averagePhotodiodes.append(round((sum(i))/(len(i)), loops))
            print(len(voltages))
            print(len(averagePhotodiodes))

            scatter = str(input("Scatter plot (y/n)? "))
            # SCATTER PLOT
            # plt.scatter(allVoltages, allPhotodiode, color = 'b')

            plt.scatter(voltages, averagePhotodiodes, color='r', zorder=2)
            if scatter == "y":
                plt.scatter(allVoltages, allPhotodiode, color = 'b')
            # plt.plot(voltages, averagePhotodiodes, color='b', zorder=1)

            # SAVGOL FILTER
            filter = str(input("Filter (y/n)? "))
            if filter == "y":
                try:
                    w = savgol_filter(averagePhotodiodes, 35, 4)
                    plt.plot(voltages, w, 'black')
                except ValueError:
                    pass

            plt.show()

            run = str(input("Ready to Run?(y/n) "))