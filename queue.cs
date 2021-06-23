using System;

namespace Queue
{
    class QueueClassNode
    {
        public QueueClassNode next;
        public int data;
        public QueueClassNode(int value)
        {
            data = value;
            next = null;

        }

        
    }
    class Queue
    {
        public int count;
        public QueueClassNode front, head,rear;

        public Queue()
        {
            front = null;
            this.count = 0;
        }


        public void enqueue(int data)
        {

            Console.Write("inserted value " + data + "\n");

            QueueClassNode node = new QueueClassNode(data);

            if(count == 0)
            {
                head = rear = node;
            }
            else
            {
                rear.next = node;
                rear = rear.next;
            }

            
            count++;
        }

        public dynamic dequeue()
        {
            QueueClassNode temp = head;
            if(count != 0)
            {
                head = head.next;
                count--;
                Console.WriteLine(temp.data + " dequeued");
                return temp.data;
            }

            else
            {
                return null;
            }
            
            



            /*while (runner != null && index == count)
            {
                Console.WriteLine("Dequeded Value is ",runner.data);
                front = runner.next;
                return;
            }

            while (runner != null && index != count)
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

            front = prev;
            prev.next = runner.next;
*/
         



        }

        public void size()
        {
            Console.WriteLine(count);
        }

        public void print()
        {
            QueueClassNode runner = head;

            while (runner != null)
            {

                Console.Write("| " + runner.data + " |\n");
                runner = runner.next;
            }
            Console.Write("\n");

        }

        public void reverse()
        {
            QueueClassNode runner = head, prev = null,next=null;

            if (runner == null)
            {
                return;
            }

            while (runner != null)
            {
                next = runner.next;
                runner.next = prev;
                prev = runner;
                runner = next;

            }

            head = prev;
        }

    }
class Program
    {
        static void Main(string[] args)
        {
            Queue queue = new Queue();
            queue.enqueue(1);
            queue.enqueue(10);
            queue.enqueue(100);
            queue.enqueue(1000);

            //queue.size();

           /* queue.dequeue();
            queue.print();
            queue.dequeue();*/
            queue.print();

            queue.reverse();

            queue.print();

            queue.size();



            Console.WriteLine();
        }
    }
}
