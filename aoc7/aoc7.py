import re

FILESIZE = 100000000000000000000

class directory:
    def __init__(self, size=0, name='root', parent=None):
        self.name = name
        self.size = size                    #size of files in this directory, excluding child folders
        self.parent = parent
        self.children = []
    
    def add_child(self, child_node):
    #creates a parent-child relationship
        print("Adding " + child_node.size)
        self.children.append(child_node)


def main():
    root = directory()
    nav = root
    with open('input7.txt') as f:
        input = f.readlines()
        for text in input:
            text = text.strip()
            print('======================================')

            if text == '$ ls' or text == '$ cd /':
                pass

            elif text == '$ cd ..':
            #moving out
                nav = move_out(nav)

            elif text.startswith('$ cd'):
            #moving in
                name = text.split('$ cd ')[1]
                nav = move_in(nav, name)

            else:                         
            #currently in ls -- populating current dir
                populate_dir(nav, text)

    print('== Calculating directory sizes =================')
    #Calculate all file sizes:
    root_size, smol_dir = file_size(root)
    print(root_size, smol_dir)
    print('Total size of smol directories is ', sum(smol_dir))

    print('== PART2 =================')
    space_req = 3*10**7 - (7*10**7 - root_size)
    print('Space required is ', space_req)
    maxi = 3*10**7
    for i in smol_dir:
        if i > space_req:
            maxi = min(maxi, i)
    print('We should delete the directory of size ', maxi)

def move_out(self):
#moves out one directory ---- cd ..
    if self.parent == None:
        print("THIS IS THE ROOT NODE!!!")
    print('Moved out of nav ', self.name, ' into parent ', self.parent)
    return self.parent


def move_in(self, name):
#moves in one directory ---- cd self
    for child_node in self.children:
        if child_node.name == name:
            print('Moved from nav ', self.name, ' into child ', child_node.name)
            return child_node
            

def populate_dir(self, text):
#populate the directory ---- ls
    if text[0].isdigit():
    #text is a file with a size.
        size = int(re.match('([^\s]+)', text)[0])
        self.size += size         #int(''.join(re.findall('[0-9]+', x)))
        print('File of size ', size, 'added to ', self.name)
    else:
    #text is a subdirectory -- dir abcd
        self.children.append(directory(name=text.split('dir ')[1], parent=self))
        print('Child ', text.split('dir ')[1], 'created with parent ', self.name)

def file_size(self, filesize=FILESIZE):
    smol_dir = []
    for child_node in self.children:
        x = file_size(child_node)
        self.size += x[0]
        smol_dir.extend(x[1])
    if self.size <= filesize:
        smol_dir.append(self.size)
    return self.size, smol_dir
main()