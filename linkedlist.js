function linkedList() {
    this.head = null;
    this.count = 0
    this.tail = null;

    this.push = function (val) {
        if (this.tail)

            this.tail = val;
        this.head = this.tail



        this.count++;

    }
}


function node(val) {
    this.value = val;
    this.next = null
}


llh = new linkedList()

llh.push(new node(1));
llh.push(new node(4));
console.log(llh);
