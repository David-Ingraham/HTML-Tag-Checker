from ArrayStack import ArrayStack
import os 
import re
import sys

def readFile(path: str) -> str:

    """
    Reads and returns the content of a file given its file path.
    
    Args:
        path (str): The file path to the file to be read.
        
    Returns:
        str: The content of the file as a string.
        
    Raises:
        FileNotFoundError: If the file or directory at the given path cannot be found.
    """

    if not os.path.isfile(path):
        msg = f'{path} file or directory cannot be found'
        raise FileNotFoundError(msg)

    with open(path) as f:
        data = f.read().strip()

    return data



def parseHTML(htmlStr: str)-> bool: #if false print out whih tags were missed 
    #as soon as you see a tag that closes, the top item on the stack has to be the matching opening 
    #build up the


    """
    Parses an HTML string to check for matching opening and closing tags.
    
    This function uses a stack to keep track of opening tags and ensures that
    every opening tag has a corresponding closing tag in the correct order.
    It prints out unmatched tags if found.
    
    Args:
        htmlStr (str): The HTML string to be parsed.
        
    Returns:
        bool: True if all tags match correctly, False otherwise.
    """

    stack = ArrayStack()
    pattern = r'<(\w+).*?>|</(\w+)>'

    
    tagList : list = re.findall(pattern, htmlStr)


    for i in  range(len(tagList)):

        if tagList[0][0] == '':
            print(f'unmatched </{tagList[0][1]}> ')
            return False #if the first tag is closing tag, return false 
        
        if tagList[i][1] == '': #each item in the taglist is a tuple, and the second item being blank means its a opening tag
            stack.push(tagList[i][0])   
        else:
            if stack.top() != tagList[i][1]:
                print(f'mismatched <{stack.pop()}> to </{tagList[i][1]}>')
                return False
            stack.pop()
            

    if stack.is_empty(): return True

    if not stack.is_empty(): 
        res=[]
        for i in range(len(stack)):
            res.append(f'<{stack.pop()}>')

        x = " ".join(res[::-1])

        
        print(f'unmatched tags: {x}')
        return False


    #for tag in tagList:
     #   if not stack.is_empty():
      #      if tag[1] == '':
       #         stack.push(tag[0])
        #    else:
         #       return False 
 
    #if find a closing tag, the item at the top of the stack has to be the corespongin opening tag to the current tag i looking at.
                #if the closing tag i found matches the top of the stack then pop the elementsfrom the stack 
                #IF WE HAVE GONE THRU WHOLE STR AND STACK is not empty, then there are unmatched tags 


    #print(tagList)


    print(stack)


def main() -> None:
    """
    The main function that executes the program.
    
    It reads the file path from command line arguments, reads the file content,
    and then parses the HTML content from the file. It prints whether the HTML
    is correctly formatted with matching tags.
    
    Raises:
        IndexError: If an incorrect number of command line arguments is provided.
    """

    if len(sys.argv) != 2: 
        raise IndexError(f'Incorrect Number of arguments. Needs 2, received {len(sys.argv)}')
    
        sys.exit(2)

    try:
        data = readFile(sys.argv[1])

    except FileNotFoundError:
        print(f'{sys.argv[1]} file or directory cannot be found')
        sys.exit(1)

    except IndexError:
        print(f'Incorrect Number of arguments. Needs 2, received {len(sys.argv)}')
        sys.exit(2)

        
    
    print(parseHTML(data))



if __name__ == '__main__':
    main()