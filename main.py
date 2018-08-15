
import csv          # need to import the csv module

csv_path = 'raw_data/election_data_1.csv'

csv_file = open (csv_path, 'r')
csv_reader = csv.reader(csv_file, delimiter=',')

# for line in csv_reader:
#     print(line)

csv_file.seek(0)


def resetFileToBeginning():
    csv_file.seek(0)


def calculateTotalNumberofVotesCasted():

    resetFileToBeginning()
    next(csv_reader)  # skip the first line in the file, which is the header

    count_of_casted_votes = 0
    for row in csv_reader:
        if row[0] != " ":
            count_of_casted_votes = count_of_casted_votes + 1
        else:
            break

    return count_of_casted_votes


def completeListOfCandidateswithVotes():

    resetFileToBeginning()
    next(csv_reader)  # skip the first line in the file, which is the header

    list_of_candidates_with_votes = []
    number_of_casted_votes = 0

    for row in csv_reader:
        if row[0] != " ":
            list_of_candidates_with_votes.append(row[2])
            number_of_casted_votes = number_of_casted_votes + 1
        else:
            break

    unique_list_of_candidates_with_votes = set(list_of_candidates_with_votes)
    return unique_list_of_candidates_with_votes


def find_offset_for_candidate_in_list(list_of_candidates, name_of_candidate):

    # go through the list of candidates and find the offset for the candidate
    for i in range(0, len(list_of_candidates), 1):
        if (list_of_candidates[i] == name_of_candidate):
            return i

    return 0           # returning a 0 to indicate that the list was exhausted and the name was not found


def calc_total_votes_for_each_candidate(list_of_candidates):

    candidate_vote_count = []       # This is a list that will keep each candidates total votes

    # We will initialize the candidates_vote_count list to all zeroes for each candidate to begin with
    for index in range(0, len(list_of_candidates), 1):
        candidate_vote_count.append(0)                      # we need to append to the empty list. We can not
                                                            # just set the offset as [index], in python, since the list is empty

    resetFileToBeginning()
    next(csv_reader)  # skip the first line in the file, which is the header

    for row in csv_reader:
        name_of_candidate = row[2]

        offset = find_offset_for_candidate_in_list(list_of_candidates, name_of_candidate)

        candidate_vote_count[offset]  += 1                  # increment the candidates vote count

    return candidate_vote_count


def print_candidates_total_votes(list_of_candidates, list_of_candidates_total_votes, total_number_of_cast_votes):

    print('\n')
    print('Election Results',)
    print('-------------------------',)
    print('Total Votes: ' + str(total_number_of_cast_votes) ,)
    print('------------------------- ',)

    for index in range(0, len(list_of_candidates), 1):
        name_of_candidate = list_of_candidates[index]
        total_votes_for_candidate = list_of_candidates_total_votes[index]

        percentage_for_candidate = total_votes_for_candidate / total_number_of_cast_votes
        actual_percentage_for_candidate = percentage_for_candidate * 100


        print(name_of_candidate + ':' + ' ' + str(actual_percentage_for_candidate) + '% ' + '(' + str(total_votes_for_candidate) + ')' ,)

    return actual_percentage_for_candidate


def determine_candidate_with_max_votes(list_of_candidates, list_of_candidates_total_votes):

    max_value = max(list_of_candidates_total_votes)
    index = list_of_candidates_total_votes.index(max_value)

    candidate_name = list_of_candidates[index]

    print('-------------------------',)
    print('Winner: ' + candidate_name ,)
    print('-------------------------',)

    return candidate_name


def write_output_resulting_file(list_of_candidates, list_of_candidates_total_votes, total_number_of_cast_votes, candidate_with_max_votes):

    with open('raw_data/output_result.txt', 'w') as outputFile:
        outputFile.write('\n')
        outputFile.write('Election Results', )
        outputFile.write('\n')
        outputFile.write('-------------------------', )
        outputFile.write('\n')
        outputFile.write('Total Votes: ' + str(total_number_of_cast_votes), )
        outputFile.write('\n')
        outputFile.write('------------------------- ', )
        outputFile.write('\n')

        for index in range(0, len(list_of_candidates), 1):
            name_of_candidate = list_of_candidates[index]
            total_votes_for_candidate = list_of_candidates_total_votes[index]

            percentage_for_candidate = total_votes_for_candidate / total_number_of_cast_votes
            actual_percentage_for_candidate = percentage_for_candidate * 100

            outputFile.write(name_of_candidate + ':' + ' ' + str(actual_percentage_for_candidate) + '% ' + '(' + str(total_votes_for_candidate) + ')' + '\n' )

            outputFile.write('-------------------------', )

            outputFile.write('\n')

        outputFile.write('Winner: ' + candidate_with_max_votes ,)

        outputFile.write('\n')

        outputFile.write('-------------------------',)








def startProcess():

    total_number_of_cast_votes = calculateTotalNumberofVotesCasted()
    set_of_candidates = completeListOfCandidateswithVotes()
    list_of_candidates_total_votes = calc_total_votes_for_each_candidate(list(set_of_candidates))

    list_of_candidates = list(set_of_candidates)
    print_candidates_total_votes(list_of_candidates, list_of_candidates_total_votes, total_number_of_cast_votes)

    candidate_with_max_votes = determine_candidate_with_max_votes(list_of_candidates, list_of_candidates_total_votes)

    write_output_resulting_file(list_of_candidates, list_of_candidates_total_votes, total_number_of_cast_votes, candidate_with_max_votes)


startProcess()