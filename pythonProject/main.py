# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    from pystrich.datamatrix import DataMatrixEncoder
    encoder = DataMatrixEncoder(""""JAMEL EDDINE",
              lastName: "GABTNI",
              vaccinationAgent1: "Hattab Samia",
              vaccinationAgent2: "NAFFATI MEHDI",dqshfsqjhsqqsdqsd""""")
    encoder1 = DataMatrixEncoder("""" vaccinationCenter1: "MAISON DES JEUNES SIDI SALEM -BIZERTE VILLE",
              vaccinationCenter2: "MAISON DES JEUNES SIDI SALEM -BIZERTE VILLE",""")
    encoder2 = DataMatrixEncoder(""""
              vaccinationCertificateId:
                "evax-certif-9c2f38bf-ab77-4aed-951e-6fee29e932af",
                  """"")
    encoder3 = DataMatrixEncoder(""""
                  jkQDBZKHDBAZJHVDAZHJDVAZVDAZHJVDAZHJVDJHVDHAJZVDAZJHVDYAZVYAZVAZVDYUVEAZJHVEAZ
                      """"")
    encoder4 = DataMatrixEncoder(""""
                      G
                          """"")

    encoder.save("datamatrix_test.png")
    encoder1.save("datamatrix_test.png")
    encoder2.save("datamatrix_test.png")
    encoder3.save("datamatrix_test.png")
    encoder4.save("datamatrix_test.png")





    #print(encoder.get_ascii())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
