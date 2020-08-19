
def main():
    # sem patri veskery kod
    print("tady zacinam")
    print (secti(5,3,4))
    print(scitani(3,1))

def scitani(a,b=5):
    return a+b

def secti(*co):
    return sum(co)

if __name__ == "__main__":
    main()
