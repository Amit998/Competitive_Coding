
using System;

namespace HashTable
{
    public class Node
    {
        public int key;
        public dynamic data;
        public Node next;
    }

    public class HashTable
    {
        int count;
        Node mainNode;

        public HashTable()
        {
            this.count = 0;
            mainNode = null;
        }

        public Node newNode(int key, dynamic data)
        {
            Node temp = new Node();
            temp.key = key;
            temp.data = data;
            temp.next = null;
            count++;
            return temp;
        }

        public void Add(int key, dynamic data)
        {
            Node start = mainNode;
            Node head = mainNode;
            Node temp = newNode(key,data);

            

            if(mainNode == null)
            {
                mainNode = temp;
            }
            else if(!contain(key))
            {

                if(head.key > key)
                {
                    temp.next = head;
                    head = temp;
                }
                else
                {
                    while (start.next != null && start.next.key < key)
                    {
                        start = start.next;
                    }
                    temp.next = start.next;
                    start.next = temp;
                }
                mainNode = head;
            }
            else
            {
                Node runner = mainNode;
                while (runner != null)
                {
                    if (runner.key == key)
                    {

                        runner.data = data;
                        
                    }
                    runner = runner.next;
                }
            }

        }

        public void size()
        {
            Console.WriteLine("Size Of The Queue is " + count);
        }

        public void print()
        {
            Node runner = mainNode;
            while (runner != null)
            {
                Console.Write(runner.key + " is key " +runner.data+"\n");
                runner = runner.next;
            }
        }

        public bool isEmpty()
        {
            Node head = mainNode;
            return head == null ? true : false;
        }


        public bool contain(int key)
        {
            Node head = mainNode;
            if (isEmpty())
            {
                return false;
            }

            if (head.key == key)
            {
                return true;
            }

            while (head != null)
            {
                if (head.key == key)
                {
                    return true;
                }

                head = head.next;
            }
            return false;
        }


        public void remove(int key)
        {
            Node runner = mainNode;
            Node prev = null;
            count--;

            
            while (runner != null && runner.key == key)
            {
                //Console.WriteLine("first");
                mainNode = runner.next;
                return;
            }

            while (runner != null && runner.key != key)
            {
               
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
        

        public dynamic get_value_by_id(int key)
        {
            Node runner = mainNode;
            bool flag = false;
            dynamic value=null;

            if (isEmpty())
            {
                return "Ëmpty";
            }
            else
            {
                while(runner != null)
                {
                    if(runner.key == key)
                    {
                        flag = true;
                        value = runner.data;
                        break;
                    }
                }
            }

            if (flag)
            {
                return value;
            }
            else
            {
                return "no data found";
            }


            
        }
    
    }


    class Program
    {
        static void Main(string[] args)
        {
            HashTable ht = new HashTable();
            ht.Add(1, "A");
            ht.Add(1, "AFF");
            ht.Add(2, "B");
            ht.Add(3, "C");
            ht.Add(4, "D");
            ht.Add(5, "E");

            //ht.print();
            ht.remove(3);
            ht.print();
            ht.size();



            Console.WriteLine(ht.get_value_by_id(1));
            //Console.WriteLine(ht.contain(1));


            Console.ReadKey();
        }
    }
}
