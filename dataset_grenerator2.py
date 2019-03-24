from dataset import interest_div
import csv

pos = [-1] * 30


with open('data.csv') as csvfile:
    data = csv.reader(csvfile, delimiter=",")
    test = []
    rownumber = -1

    for row in data:
        test.append(row)
    test.remove(test[0])

    for row in test:
        rownumber += 1
        max_value = 0
        rowcnumber = -1
        for rowC in test:
            rowcnumber += 1
            score = 0
            if row[2] == rowC[5] and row[3] == rowC[6]:
                score += 10
            if row[9] != rowC[9]:
                score += 10
            dif_int = abs(interest_div[rownumber] - interest_div[rowcnumber])
            score += dif_int * 2
            if score > max_value:
                max_value = score
                pos[rownumber] = rowcnumber + 1
print(pos)

with open('data.csv',"r") as csvfile_in, open("data_New.csv","w") as csvfile_Out:

    rdr = csv.DictReader(csvfile_in)
    newfieldnames = rdr.fieldnames
    newfieldnames.append("match")
    wrtr = csv.DictWriter(csvfile_Out, fieldnames= newfieldnames)
    wrtr.writeheader()
    for row_id, row in enumerate(rdr, start = 0):
        row['match'] = pos[row_id]
        wrtr.writerow(row)





