using System;

namespace stack
{
    class StackClassNode
    {
        public StackClassNode next;
        public int data;
        public StackClassNode(int value)
        {
            data = value;
            next = null;

        }
    }



    class Stack
    {
        int count;
        StackClassNode top;
        public Stack()
        {
            top = null;
            this.count = 0;
        }

        public void push(int data)
        {
            Console.Write("inserted value "+data+"\n");
            StackClassNode node = new StackClassNode(data);
            node.next = top;
            top = node;
            count++;

        }

        public void size()
        {
            Console.WriteLine(count);
        }

        public void printStack()
        {
            StackClassNode runner = top;

            while(runner != null)
            {

                Console.Write("| "+runner.data+" |\n");
                runner = runner.next;
            }
            Console.Write("\n");

        }

        public int pop()
        {
            StackClassNode runner = top;

            int val;
            count--;
            val = runner.data;
            top = runner.next;
            Console.Write("popped value " + val + "\n");
            return val;
        }

        public bool contain(int data)
        {
            StackClassNode runner = top;

            while (runner != null)
            {

                if(data == runner.data)
                {
                    return true;
                }
                runner = runner.next;
            }
            return false;
        }

        public int peek()
        {
            return top.data;
        }

        public StackClassNode reveserAll()
        {

            StackClassNode runner=top, prev = null;

            if (runner == null)
            {
                return runner;
            }

            while(runner != null)
            {
                StackClassNode next = runner.next;
                
                runner.next = prev;
                prev = runner;
                
                runner = next;
                
            }

            top = prev;

            return top;
        }

    }
    class Program
    {
        static void Main(string[] args)
        {
            Stack st = new Stack();
            st.push(1);
            st.push(2);
            st.push(3);
            st.push(4);

            //st.size();
            //st.printStack();
            st.pop();
            st.pop();
            st.printStack();
            //st.printStack();

            //Console.Write(st.contain(1));

            st.reveserAll();
            st.printStack();

            Console.WriteLine("");
        }
    }
}
