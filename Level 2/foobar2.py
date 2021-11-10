def solution(h, q):
    # Your code here

    parents = []

    for element in q:
        number = (2**h)-1

        if element == number:
            parents.append(-1)

        else:

            parent = number
            node = number

            while True:
                number = number >> 1
                leftNode = node-1
                rightNode = node-number-1

                if (element is rightNode) or (element is leftNode):
                    parents.append(parent)
                    break

                elif element < rightNode:
                    node = rightNode
                elif element > rightNode:
                    node = leftNode

                parent = node


    return parents

print(solution(3, [7, 3, 5, 1]))
