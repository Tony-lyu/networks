# network-proj2

I divide my code into 2 sections: one is a FTPClient class that contains all the methods to connect, login, close, and execute commands. The other part is my main class where I parse the commands. The first challenge for me is to establish the second data channel. This is new to me so I had to do some research. The second challenge for me is to debug. I have to print out the response from FTP server and sepcify which response is from control socket and which one is from the data socket. 

To test my code, I created a file in my folder called testupload.txt, and I did the following steps: 
1. create a folder on FTP server called dir1, and then call ls on the root to make sure my mkdir and ls functions correctly
2. cp the testupload.txt file to the server and save it as /dir1/testupload.txt, then ls dir1 to check if upload is successful
3. cp dir1/testupload.txt and save it as testdownload.txt to my local machine, then open the file to check if the text in it is unchanged
4. mv local file testdownload.txt to the server and save it as /dir1/testmv.txt, then check if my local file is deleted, and ls /dir1 to check the upload
5. mv dir1/testmv.txt and save it to my local machine called testmv.txt, then ls /dir1 to check if the file is deleted, and open it on my local machine
6. rm /dir1/testupload.txt, and then rmdir /dir1. ls after each step to verify deletion. 
From the steps above, I tested every command and verified their correctness. 
