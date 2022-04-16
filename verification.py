import helper


# Test whether company name exists in the data
# def companyExist(input, filename):
#     data = helper.readFile(filename)
#     dicVal = data.values()
#     if input in dicVal.values(1):
#         return True

# Check whether column name exists in the data
def columnTest(input, filename):
    data = helper.readFile(filename)
    dicVal = data.values()
    if input in dicVal.keys():
        return True