using System;

namespace Tree
{
    class QueueNode
    {
        public QueueNode next;
        public int data;
        public QueueNode(int value)
        {
            this.data = value;
            next = null;
        }
    }
    class Queue
    {
        public int count;
        public QueueNode front, rear,head;

        public Queue()
        {
            front = null;
            this.count = 0;
        }

        public bool isEmpty()
        {
            if (count == 0) {
                return true;
            }
            return false; 
        }

        public void enqueue(int data)
        {
            QueueNode node = new QueueNode(data);

            if (count == 0)
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

        public dynamic deQueue()
        {

            QueueNode temp = head;
            if (count != 0)
            {
                head = head.next;
                count--;
                //Console.WriteLine(temp.data + " dequeued");
                return temp.data;
            }

            else
            {
                return null;
            }


        }
        public void print()
        {
            QueueNode runner = head;

            while (runner != null)
            {

                Console.Write("| " + runner.data + " |\n");
                runner = runner.next;
            }
            Console.Write("\n");

        }



    }
    class Node
    {
        public int value;
        public Node left,right;

        public Node(int initial)
        {
            value = initial;
            right=left = null;
            
        }

    }

    class NTree
    {
        Node top;
        int level;
        int rootNode;

        public NTree()
        {
            this.level = 0;
            top = null;
        }
        public NTree(int initial)

        {
            rootNode = initial;
            top = new Node(initial);
        }

        public void Add(int value)
        {
            if(top == null)
            {
                Node newNode = new Node(value);
                top = newNode;
                return;
            }

            Node currentNode = top;
            bool added = false;

            do
            {
                if (value < currentNode.value)
                {
                    if(currentNode.left == null)
                    {
                        Node newNode = new Node(value);
                        currentNode.left = newNode;
                        added = true;
                    }
                    else
                    {
                        currentNode = currentNode.left;
                    }
                }
                if (value >= currentNode.value)
                {
                    if (currentNode.right == null)
                    {
                        Node newNode = new Node(value);
                        currentNode.right = newNode;
                        added = true;
                    }
                    else
                    {
                        currentNode = currentNode.right;
                    }

                }
            } while (!added);


        }

        public void AddRc(int value)
        {
            AddR(ref top, value);
        }

        public void AddR(ref Node N,int value)
        {
            if (N == null)
            {
                Node newNode = new Node(value);
                N = newNode;
                return;
            }
            if(value < N.value)
            {
                AddR(ref N.left, value);
                return;
            }
            if(value >= N.value)
            {
                AddR(ref N.right, value);
                return;
            }
        }

        public Node deleteRec(Node root, int key)
        {
            if (root == null)
            {
                return root;
            }

            if(key < root.value)
            {
                root.left = deleteRec(root.left, key);
            }
            else if (key > root.value)
            {
                root.right= deleteRec(root.right, key);
            }
            else
            {
                if(root.left == null)
                {
                    return root.right;
                }else if(root.right == null)
                
                    return root.left;
                

                root.value = minValue(root.right);
                root.right = deleteRec(root.right, root.value);
            }

            return root;
        }

        int minValue(Node root)
        {
            int minv = root.value;

            while(root.left != null)
            {
                minv = root.value;
                while(root.left != null)
                {
                    minv = root.left.value;
                    root = root.left;
                }
            }

            return minv;
        }
        public void contains(int value)
        {
            Node root = top;
            bool flag = false;
            Console.WriteLine(containRec(root,value,ref flag));
        }

        public bool containRec(Node root,int value,ref bool flag)

        {
            if(root == null)
            {
                return false;
            }
     
            else if (root != null)
            {
                if(root.value == value)
                {
                    flag = true;
                    
                }
                
                containRec(root.left,value,ref flag);
                containRec(root.right,value,ref flag);
            }

  

            return flag;

            /*if(root.value == value)
            {
                return true;
            }
            else if(root.left != null)
            {
                containRec(root.left, value);
                

            }else if (root.right != null)
            {
                containRec(root.right, value);
            }*/


        }
        public void delete(int key)
        {
            Node root = top;
          

            if (root == null)
            {
                Console.WriteLine("Empty");
                return;
            }

            top = deleteRec(root,key);
      
        }

        public void printRe() {

            string myStr = "";
            Print(null,ref myStr);
            Console.WriteLine(myStr);
        }



        public void Print(Node N,ref string s)
        {
           
            
            if(N == null)
            {
                N = top;
            }
            if(N.left != null) {
                Print(N.left,ref s);
                s = s + N.value.ToString()+"-";
            }
            else
            {
                s = s + N.value.ToString()+"-";
            }
            if(N.right != null)
            {
                Print(N.right,ref s);
            }
        }

        public void inorder()
        {
            inorderRec(top);
            Console.WriteLine('\n');
        }

        public void inorderRec(Node root)
        {
            if(root != null)
            {
                inorderRec(root.left);
                Console.Write(root.value+"-");
                inorderRec(root.right);
            }

        }

        public void getLeve()
        {
            Console.Write(level);
        }
        public void height()
        {
            Console.WriteLine(heightHelper(top)+"Height");
        }
        public int heightHelper(Node node)
        {
            if (node == null)
            {
                return 0;
            }
            else
            {
                int left_height = heightHelper(node.left);
                int right_height = heightHelper(node.right);

                if(left_height > right_height)
                {
                    return left_height + 1;
                }
                else
                {
                    return right_height + 1;
                }
            }
        }

        public void DFS()
        {
            /* inorder,preorder,postorder */
            string inorderString = "";
            string preorderString = "";
            string postOrderString = "";

            Node node = top;
            Console.WriteLine(" Inorder");
            inOrder(node,inorderString);
            Console.WriteLine("\n prorder");
            preOrder(node, preorderString);
            Console.WriteLine("\n Postorder");
            postOrder(node, postOrderString);


        }

        public void BFS()
        {
            Node node = top;
            Console.WriteLine("BFS");
            levelOrderTraversal(node);
        }

        public void inOrder(Node node,string inorderString)
        {
            if(node == null)
            {
                return;
            }

            inOrder(node.left,inorderString);
            Console.Write(node.value+"->");
            inOrder(node.right,inorderString);

        }

        public void preOrder(Node node, string preOrderString)
        {
            if (node == null)
            {
                return;
            }

            Console.Write(node.value + "->");
            preOrder(node.left, preOrderString);
            preOrder(node.right, preOrderString);
        }

        public void postOrder(Node node, string postOrderString)
        {
            
            preOrder(node.left, postOrderString);
            preOrder(node.right, postOrderString);
            Console.Write(node.value + "->");
        }

        public void get_level_value(int level)
        {

            currentLevelValue(top, level);
        }

        public void currentLevelValue(Node node,int level)
        {
            if(node == null)
            {
                return;
            }
            if (level == 1)
            {
                Console.WriteLine(node.value );
            }else if(level > 1)
            {
                currentLevelValue(node.left,level-1);
                currentLevelValue(node.right, level - 1);
            }

        }

        public void levelOrderTraversal(Node node)
        {
            Queue queueTest = new Queue();
            

            //Console.WriteLine(rootNode);

            //Console.WriteLine(queueTest.isEmpty());
            queueTest.enqueue(rootNode);
            //Console.WriteLine(queueTest.isEmpty());


            while (!queueTest.isEmpty())
            {
                //Node node= queueTest.deQueue();
                Console.WriteLine();


                if (node.left != null)
                {
                    queueTest.enqueue(node.left.value);
                }

                if (node.right != null)
                {
                    queueTest.enqueue(node.right.value);
                }

            }



        }


    }



    class Program
    {
        static void Main(string[] args)
        {

         
            NTree myTree = new NTree(10);

            myTree.AddRc(1);
            myTree.AddRc(11);
            myTree.AddRc(2);
            myTree.AddRc(3);
            myTree.AddRc(4);
            myTree.AddRc(5);
            myTree.BFS();
            /* myTree.AddRc(22);
             myTree.AddRc(6);
             myTree.AddRc(32);
             myTree.AddRc(9);*/

            //myTree.get_level_value(2);


            //myTree.inorder();

            //myTree.printRe();
            //myTree.DFS();

            /*Queue queue = new Queue();
            queue.enqueue(1);
            queue.enqueue(10);
            queue.enqueue(100);
            queue.enqueue(1000);

            queue.deQueue();
            queue.print();
            queue.deQueue();
            queue.print();*/



            //myTree.delete(1);
            //myTree.delete(32);
            //myTree.delete(12);
            //myTree.inorder();
            //myTree.contains(9);

            Console.ReadKey();
        }
    }
}


//https://www.journaldev.com/44201/breadth-first-search-depth-first-search-bfs-dfs
