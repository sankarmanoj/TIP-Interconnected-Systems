package com.sankarmanoj.tip;
import android.content.Context;
import android.widget.Toast;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.Socket;

public class NetworkThread implements Runnable
{
    Context context;
    PrintWriter output = null;
    BufferedReader input = null;
    NetworkThread(Context context)
    {

        this.context= context;
    }

    public PrintWriter getOutput() {
        if(output==null)
        {
            throw new RuntimeException("Streams not initialized");
        }
        return output;
    }

    public BufferedReader getInput() {
        if(input==null)
        {
            throw new RuntimeException("Streams not initialized");
        }
        return input;
    }

    @Override
    public void run() {
        try {
            Socket socket = new Socket("sankar-manoj.com", 4565);
            output = new PrintWriter(new OutputStreamWriter(socket.getOutputStream()));
            input = new BufferedReader(new InputStreamReader(socket.getInputStream()));
        }
        catch (IOException e)
        {
            Toast.makeText(context, "Unable to connect", Toast.LENGTH_SHORT).show();
            e.printStackTrace();
        }
    }

}