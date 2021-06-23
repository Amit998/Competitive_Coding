using System;

namespace PriorityQueue
{
    public class Node
    {
        public int data;
        public int priority;
        public Node next;
    }

    public class PriorityQueueNode
    {
        int count;
        Node mainNode;

        public PriorityQueueNode()
        {
            mainNode = null;
            this.count = 0;

        }

        public Node newNode(int data,int priority_val)
        {

            Node temp = new Node();
            temp.data = data;
            temp.priority = priority_val;
            temp.next = null;
            count++;
            return temp;
        }

        public int peek()
        {
            Node head = mainNode;
            //Console.WriteLine("\n"+head.data+"this is test");
            return head.data;
        }

        public void size()
        {
            Console.WriteLine("Size Of The Queue is "+count);
        }

        public void print()
        {
            Node runner = mainNode;
            while (runner != null)
            {
                Console.Write(runner.data + "  ");
                runner = runner.next;
            }
        }


        public void enqueue(int data,int priority_val)
        {

            Node start = mainNode;

            Node temp =newNode(data,priority_val);
            Node head = mainNode;

            if(mainNode == null)
            {
                mainNode = temp;
            }
            else
            {
                if (head.priority > priority_val)
                {
                    temp.next = head;
                    head = temp;
                   
                    //count++;
                }
                else
                {
                    while (start.next != null && start.next.priority < priority_val)
                    {
                        start = start.next;
                    }
                    temp.next = start.next;
                    start.next = temp;
                    //count++;
                }
                mainNode = head;
            }
        }

        public void dequeue()
        {
            Node head = mainNode;
            count--;
            Console.WriteLine("Dequeued Value is "+head.data);
            mainNode = head.next;
            
        }

        public void printNode(Node runner)
        {
            while (runner != null)
            {
                Console.Write(runner.data + "  ");
                runner = runner.next;
            }
        }

        public bool isEmpty()
        {
            Node head = mainNode;
            return head == null ? true : false;
        }

        public Node reverse()
        {
            Console.WriteLine("\nreverse");
            Node runner = mainNode,prev=null;

            if(runner == null)
            {
                Console.WriteLine("Empty ");
                return runner;
            }

            while (runner != null)
            {
                Node next = runner.next;
                //Console.Write("\n  "+runner.data);
                runner = prev;
                prev = runner;
                runner = next;
            }

            //printNode(prev);
            mainNode = prev;


            return mainNode;
        }

        public bool contain(int data)
        {
            Node head = mainNode;
            if (isEmpty())
            {
                return false;
            }

            if(head.data == data)
            {
                return true;
            }

            while(head != null)
            {
                if (head.data == data)
                {
                    return true;
                }

                head = head.next;
            }
            return false;
        }
        public Node reveserAll()
        {

            Node runner = mainNode, prev = null;

            if (runner == null)
            {
                return runner;
            }

            while (runner != null)
            {
                Node next = runner.next;

                runner.next = prev;
                prev = runner;

                runner = next;

            }

            mainNode = prev;

            return mainNode;
        }
    }



    class Program
    {
        static void Main(string[] args)
        {
            PriorityQueueNode pq =new PriorityQueueNode();
            //Node node = pq.newNode(4, 5);
            
            pq.enqueue(5, 2);
            
            pq.enqueue( 6, 3);
           
            pq.enqueue(7, 4);

            pq.enqueue(700, 1);
            pq.enqueue(700111, 0);


            //pq.size();

            //Console.WriteLine("\n");
            /*pq.print();
            Console.WriteLine("\n" + pq.peek() + " peek");
            pq.dequeue();
            pq.print();

            Console.WriteLine("\n" + pq.peek() + " peek");
            pq.dequeue();
            pq.print();


            Console.WriteLine(pq.contain(4));*/

            //pq.size();


            //pq.print();
            pq.print();
            pq.reveserAll();
            pq.print();

            //pq.size();

            //pq.print();
            // Console.WriteLine(pq.peek());

            Console.ReadLine();
        }
    }
}
