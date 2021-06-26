
using System;

namespace HashTable
{
    public class Node<T,T2>
    {
        public dynamic key;
        public T data;
        public dynamic tempValue;
        public bool isString=false;
        public Node<T,T2> next;
    }

    public class HashTable<T, T2>
    {
        int count;
        Node<T, T2> mainNode;

        public HashTable()
        {
            this.count = 0;
            mainNode = null;
        }

        public Node<T, T2> newNode(dynamic key, T data)
        {

            //Console.WriteLine((int)key+" lol" + key);
            
            /*int tempValue;*/

            /*if(key is string)
            {
                tempValue = get_asci_value_of_string(key);
            }
            else
            {
                tempValue = key;
            }*/


            Node<T, T2> temp = new Node<T, T2>();
            temp.isString = key is string;
            temp.tempValue= temp.isString ? get_asci_value_of_string((key)) : 1;

            temp.key = key;
            temp.data = data;
            temp.next = null;
            count++;
            return temp;
        }


        public int get_asci_value_of_string(string value)
        {
            int total=0;

            foreach (var c in value)
            {
                total += (int)c;
            }

            return total;
        }

        public bool isLessThen(int A,int B)
        {
            if(A < B)
            {
                return true;
            }
            else
            {
                return false;
            }


           
        }

        public int filter(Node<T, T2> head,dynamic value)
        {
            int tempValue = head.isString ? head.tempValue : head.key;
            return tempValue;
        }

        public int key_tester(dynamic value)
        {


            return value is string ? get_asci_value_of_string(value) : value;
        }

        public void Add(dynamic key,T data)
        {
            Node<T, T2> start = mainNode;
            Node<T, T2> head = mainNode;
            Node<T, T2> temp = newNode(key,data);
            int tempValue = filter(temp, temp.key);
            int key_tester_value = key_tester(key);




            if (mainNode == null)
            {
                mainNode = temp;
            }
            else if(!contain(key))
            {
                
                if (tempValue > key_tester_value)
                {
                    temp.next = head;
                    head = temp;
                }
                else
                {
                    while (start.next != null && key_tester(start.next.key) < key_tester_value)
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
                Node<T, T2> runner = mainNode;
                while (runner != null)
                {
                    if (runner.key == key_tester_value)
                    {

                        runner.data = data;
                        
                    }
                    runner = runner.next;
                }
            }

            

        }
        /*public Node<T, T2> get_Node()
        {
            return mainNode;
        }*/

        public void size()
        {
            Console.WriteLine("Size Of The Queue is " + count);
        }

        public void print()
        {
            Node<T, T2> runner = mainNode;
            while (runner != null)
            {
                Console.Write(runner.key + " is key " +runner.data+"\n");
                runner = runner.next;
            }
        }

        public bool isEmpty()
        {
            Node<T, T2> head = mainNode;
            return head == null ? true : false;
        }



        public bool contain(dynamic key)
        {
            Node<T, T2> head = mainNode;

            int tempValue = filter(head, head.key);
            int key_tester_value = key_tester(key);


            if (isEmpty())
            {
                return false;
            }

            

     

            //Console.WriteLine(tempValue+"  "+ key_tester_value);

            if (tempValue == key_tester_value)
            {
                return true;
            }

            while (head != null)
            {
                if (tempValue == key_tester_value)
                {
                    return true;
                }

                head = head.next;
            }
            return false;
        }


        public void remove(dynamic key)
        {
            Node<T, T2> runner = mainNode;
            Node<T, T2> prev = null;
            count--;

            
            while (runner != null && key_tester(runner.key) == key_tester(key))
            {
                //Console.WriteLine("first");
                mainNode = runner.next;
                return;
            }

            while (runner != null && key_tester(runner.key) != key_tester(key))
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
        

        public dynamic get_value_by_id(dynamic key)
        {
            Node<T, T2> runner = mainNode;
            bool flag = false;
            dynamic value=null;


            


            if (isEmpty())
            {
               
                return "Ëmpty";
            }
            else
            {
                
                while (runner != null)
                {
                    
                    if (key_tester(runner.key) == key_tester(key))
                    {

                        flag = true;
       
                        value = runner.data;
                        

                        break;
                    }
                    runner = runner.next;
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
        public Node<T, T2> get_main_Node()
        {
            return mainNode;
        }

    }


    class iterator<T,T2>
    {

        Node<T, T2> mainNode;

        public iterator(Node<T, T2> node)
        {
            this.mainNode = node;
        }

        public Node<T, T2> next(Node<T, T2> node)
        {
            if (node != null)
            {
                Console.WriteLine(node.key+"  "+node.data);
                return node.next;
            }
            else
            {
                Console.WriteLine("Empty Node");
                return null;
            }
        }
        public Node<T,T2> reset()
        {

            return mainNode;
        }

    }



    class Program
    {
        static void Main(string[] args)
        {
            HashTable<dynamic,dynamic> ht = new HashTable<dynamic,dynamic>();

            var options = "Please Select the options bewlow\n" +
                "1 to insert\n" +
                "2 to delete\n" +

                "3 to contain\n" +
                "4 get value by key\n" +
                "5 to get Size\n" +
                "6 to iterator\n" +
                "7 to print\n" +
                
                "Any other Key to exit";
            int user_input;

            bool flag = true;
            bool res;

            dynamic get_value;
            dynamic get_key;

            while (flag)
            {
                Console.WriteLine(options);
                res = int.TryParse(Console.ReadLine(), out user_input);
                if (!res)
                {
                    Console.WriteLine("please select Integer");
                    continue;
                }
                switch (user_input)
                {
                    case 1:
                        Console.WriteLine("Please Select Value to key ");
                        get_key = Console.ReadLine();

                        Console.WriteLine("Please Select Value to value ");
                        get_value = Console.ReadLine();
                        ht.Add(get_key, get_value);
                        break;

                    case 2:
                        Console.WriteLine("Delete");
                        Console.WriteLine("Please Select Value to key which you want to delete");
                        get_key = Console.ReadLine();

                        ht.remove(get_key);
                        break;
                    case 3:
                        Console.WriteLine("Contain");
                        Console.WriteLine("Please Select Value to key to check if its present or not");
                        get_key = Console.ReadLine();

                        ht.contain(get_key);
                        Console.WriteLine("Delete At Position");
                        break;
                    case 4:
                        Console.WriteLine("Contain");
                        Console.WriteLine("Please Select Value to key to check the value");
                        get_key = Console.ReadLine();
                        ht.get_value_by_id(get_key);
                        break;
                    case 5:
                        Console.WriteLine("get size");
                        ht.size();
                        break;
                    
                    case 6:
                        Console.WriteLine("Iterator");

                        break;

                    case 7:
                        Console.WriteLine("Printing ");
                        ht.print();
                        break;
                    default:
                        Console.WriteLine("Exit");
                        flag = false;
                        break;
                }
            }



            /*ht.Add(2, "B");
            ht.Add(3, "C");
            ht.Add("aaa", "yo");
            ht.Add("sb", "lol");
            ht.Add(4, "D");
            ht.Add("a", "A");
            ht.Add("b", "AFF");
            ht.Add(5, "E");

            //ht.print();
            //ht.size();
            //ht.remove("aaa");
            ht.print();
            //ht.size();



            //Console.WriteLine(ht.get_value_by_id("a"));


            //Console.WriteLine(ht.contain(1));

            Node<dynamic,dynamic> tempNode = ht.get_main_Node();
            iterator<dynamic, dynamic> i = new iterator<dynamic, dynamic>(tempNode);
            tempNode = i.next(tempNode);
            tempNode = i.next(tempNode);
            tempNode = i.next(tempNode);*/


            Console.ReadKey();
        }
    }
}
