import csv

def starts_with(line, search_string):
  split_line = line.split(' ')
  if split_line[0] == search_string:
    return True
  else:
    return False

# TODO - Would be nice to scrape and grab the difficulty from leetcode
def parse_line(line):
  split_line = line.split(' ')
  problem_num = split_line[1].replace('.', '')
  problem_name = ' '.join(split_line[2:]).rstrip()
  return [problem_num, problem_name]

with open('./data/leetcode-bloomberg.md', 'r') as md:
  with open('./output/output.csv', 'w', newline = '') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)

    for line in md:
      if starts_with(line, '##'):
        csv_writer.writerow(parse_line(line))
