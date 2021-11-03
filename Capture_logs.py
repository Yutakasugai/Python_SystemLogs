import os
import shutil
import datetime

# Create a time stamp
currDate = datetime.datetime.now()
currDate = currDate.strftime("%Y-%m-%d %H:%M:%S")
# print(currDate)


def main():

    try:
        # Create an array with carrying three log files
        files = ['system.log', 'wifi.log', 'install.log']

        # Define the folder name to save the above three logs inside
        folder = '{} LogCapture'.format(currDate)

        # Create a new directory for the named folder
        os.mkdir(folder)

        # Add the folder to the current path where you want the logs to save
        newDir = os.path.join(os.getcwd(), folder)

        # print(newDir)

        # Check all files inside of the array
        for file in files:

            # Define the path and specify the file what you want to capture
            src = r'/var/log/{}'.format(file)

            # Copy the specified file to the current directory you just created
            shutil.copy(src, newDir)

    except Exception as e:
        # Store all generated errors in the external file called err.log
        with open('err.log', 'a') as errFile:
            errFile.write(currDate + ' ' + str(e) + '\n')


main()
