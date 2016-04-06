package com.sankarmanoj.tip;
import android.content.Context;
import android.util.Log;
import android.widget.Toast;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.Socket;

public class NetworkThread implements Runnable
{
    String str;
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
            Socket socket = new Socket("sankar-manoj.com", 4900);
            output = new PrintWriter(new OutputStreamWriter(socket.getOutputStream()));
            input = new BufferedReader(new InputStreamReader(socket.getInputStream()));
        }
        catch (IOException e)
        {
            Toast.makeText(context, "Unable to connect", Toast.LENGTH_SHORT).show();
            e.printStackTrace();
        }

        while (true)
        {

            try {
                str = input.readLine();
                Log.d("Network Thread", str);
                MainActivity.myActivity.runOnUiThread(new Runnable(){
                    @Override
                    public void run() {
                        MainActivity.myActivity.myTextView.setText(str);
                    }
                });
            }
            catch (IOException e){
                e.printStackTrace();
                break;
            }
        }


    }

}