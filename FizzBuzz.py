def fizzBuzz(n):
    # Write your code here
    solution = []
    output_string = ""
    # i = 1
    # while i <= n:
    #     if i % 3 == 0:
    #         output_string = "Fizz"
    #     if i % 5 == 0:
    #         output_string += "Buzz"
    #     if output_string == "":
    #         output_string = str(i)
    #     print(output_string)
    #     solution.append(output_string)
    #     output_string = ""
    #     i += 1
    # return solution

    for (i) in range(n):
        num = i + 1
        if num % 3 == 0:
            output_string = "Fizz"
        if num % 5 == 0:
            output_string += "Buzz"
        if output_string == "":
            output_string = str(num)
        print(output_string)
        solution.append(output_string)
        output_string = ""





def main():
    n = 15
    fizzBuzz(n)

if __name__ == '__main__':
    main()