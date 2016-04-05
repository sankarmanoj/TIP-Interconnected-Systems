package com.sankarmanoj.tip;

import android.app.Activity;
import android.os.AsyncTask;
import android.support.v7.app.ActionBarActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.Socket;
import java.net.SocketAddress;


public class MainActivity extends Activity {

    EditText inputText;
    Button myButton;
    PrintWriter toServer;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        inputText=(EditText)findViewById(R.id.editText);
        myButton=(Button)findViewById(R.id.button);
        ServerConnect connect = new ServerConnect();
        connect.execute(null,null,null);
        View.OnClickListener buttonListener = new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String input = inputText.getText().toString();
                if(toServer!=null)
                {
                    toServer.write(input);
                    toServer.flush();
                }
                Log.d("MainActivity", input);
                inputText.setText("");
            }
        };
        myButton.setOnClickListener(buttonListener);

    }


    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }

    public class ServerConnect extends AsyncTask<Void,Void,Void>
    {
        @Override
        protected Void doInBackground(Void... voids) {
            try {
                Socket server = new Socket("sankar-manoj.com", 4565);
                OutputStream toS = server.getOutputStream();
                InputStream fromS = server.getInputStream();
                BufferedReader fromServer = new BufferedReader(new InputStreamReader(fromS));
                toServer = new PrintWriter(new OutputStreamWriter(toS));


            }
            catch (IOException e)
            {
                e.printStackTrace();
            }
            return null;
        }
    }
}
