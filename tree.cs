using System;

namespace Tree
{
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

        public NTree()
        {
            top = null;
        }
        public NTree(int initial)
        {
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
                Console.Write(root.value+" -");
                inorderRec(root.right);
            }


        }
    }



    class Program
    {
        static void Main(string[] args)
        {

         
            NTree myTree = new NTree(10);

            myTree.AddRc(1);
            myTree.AddRc(4);
            myTree.AddRc(3);
            myTree.AddRc(12);
            myTree.AddRc(30);
            myTree.AddRc(22);
            myTree.AddRc(6);
            myTree.AddRc(32);
            myTree.AddRc(9);

            
            myTree.inorder();
           

            myTree.delete(1);
            //myTree.delete(32);
            myTree.delete(12);
            myTree.inorder();
            myTree.contains(9);

            Console.ReadKey();
        }
    }
}
//https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/#:~:text=Binary%20Search%20Tree%20%7C%20Set%202%20%28Delete%29%201,the%20node%20and%20delete%20the%20inorder%20...%20
