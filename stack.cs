using System;

namespace linkedList
{
    class LinkedListNode
    {
        public int data;
        public LinkedListNode next;

        public LinkedListNode(int x)
        {
            data = x;
            next = null;
        }
    }

    class LinkedList
    {
        int count;
        LinkedListNode head;

        public LinkedList()
        {
            head = null;
            this.count = 0;
           
        }

        public void AddNode(int data)
        {
            LinkedListNode node = new LinkedListNode(data);
            node.next = head;
            head = node;
            count++;
        }

        public void DeleteNode(int given)
        {
            LinkedListNode runner = head;
            LinkedListNode prev = null;
            count--;

            while (runner != null && runner.data==given)
            {
                head = runner.next;
                return;
            }

            while(runner !=null && given != runner.data)
            {
                prev = runner;
                runner = runner.next;
            }

            if(runner == null)
            {
                return;
            }

            prev.next = runner.next;

        }

        public void AddAtPosition(int position,int data)
        {
            int index = 0;
            int temp;    
            LinkedListNode runner = head;
            if (position > count || runner.data == null)
            {
                Console.WriteLine("Position is bigger then the linkedSize");
                return;
            }
            count++;

            while (runner != null)
                {
                index++;
            
                if (index >= position)
                {
                    //Console.WriteLine(index+""+""+ position);
                    temp = runner.data;
                    runner.data = data;
                    data = temp;
           
                }
                runner = runner.next;
            }
        }

        public void DeleteAtPosition(int position)
        {
            LinkedListNode runner = head;
            LinkedListNode prev = null;
            count--;
            int index = 1;
            while (runner != null && index == position)
            {
                //Console.WriteLine("first");
                head = runner.next;
                return;
            }

            while (runner != null && index != position)
            {
                index++;
                prev = runner;
                runner = runner.next;
            }

            if (runner == null)
            {
                count++;
                return;
            }

            prev.next = runner.next;

        }

        public void getSize()
        {
            Console.WriteLine("\n"+count);
        }

        public void printAtPos(int pos)
        {
            LinkedListNode runner = head;
            int index = 1;


            while(index != pos)
            {
                runner = runner.next;
                index++;
                
            }

            Console.WriteLine(runner.data);


        }

        public void atCenter()
        {
            bool isOdd;
            int position = 1;
            int middle = (count / 2);


            if(count % 2 == 0)
            {
                printAtPos(middle);

            }
            else
            {
                printAtPos(middle+1);
            }
            //Console.WriteLine("\n" + count);
            //Console.WriteLine("\n" + middle);
        }

        public LinkedListNode reverseLL()
        {
            LinkedListNode runner = head, prev = null;

            if (runner == null)
            {
                return runner;
            }

            while(runner != null)
            {
                LinkedListNode next = runner.next;
                runner.next = prev;
                prev = runner;
                runner = next;
            }
            head = prev;
            return head;


        }



        public void printList()
        {
            LinkedListNode runner = head;
            
            while (runner != null)
            {
                Console.Write(runner.data+"->");
                runner = runner.next;
            }
            Console.Write("NULL  \n");
        }

        public void iterateLL()
        {
            LinkedListNode runner = head;

            while (runner != null)
            {
                Console.Write(runner.data + "\n");
                runner = runner.next;
            }

        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            LinkedList linkedList = new LinkedList();

            linkedList.AddNode(1);
            linkedList.AddNode(2);
            linkedList.AddNode(13);
            linkedList.AddNode(14);
            linkedList.AddNode(24);
            linkedList.AddNode(4);
            //linkedList.AddNode(42);
            //linkedList.printList();
            //linkedList.getSize();

            //linkedList.AddAtPosition(100, 10000);
            //linkedList.printList();

            //linkedList.DeleteNode(13);
            linkedList.printList();
            //linkedList.DeleteAtPosition(3);
            //linkedList.printList();
            //linkedList.atCenter();
            linkedList.reverseLL();
          
            linkedList.printList();



            Console.ReadKey();
        }
    }
}
