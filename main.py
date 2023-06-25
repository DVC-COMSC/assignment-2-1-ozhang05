def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """

    males = input("Input the number of males: ")
    females = input("Input the number of females: ")
    total = int(males) + int(females)
    m_perc = 100*int(males)/total
    f_perc = 100*int(females)/total

    print ("Total number of students: " + str(total))
    print ("The number of males and females: " + str(males) + ", " + str(females))
    print ("The percentages of males and females: " + str(format(m_perc, '.2f')) + ", " + str(format(f_perc, '.2f')))

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()
