from datastructures.bag import Bag

def main():
    
    bag = Bag()
    bag.add('apple')
    bag.add('pear')

    item = bag.distinct_items()

    print(f"Distinct items: (items)")



if __name__ == '__main__':
    main()
