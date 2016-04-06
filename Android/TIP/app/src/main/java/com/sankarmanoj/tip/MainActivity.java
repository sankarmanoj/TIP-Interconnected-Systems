package com.sankarmanoj.tip;

import android.app.Activity;
import android.content.Context;
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
import android.widget.Toast;

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

    TextView myTextView;
    Button myButton;
    EditText myEditText;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        final NetworkThread myNetwork = new NetworkThread(getApplicationContext());
        new Thread(myNetwork).start();
        myTextView=(TextView)findViewById(R.id.textView);
        myButton=(Button)findViewById(R.id.button);
        myEditText = (EditText)findViewById(R.id.editText);
        View.OnClickListener myListener = new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String input = myEditText.getText().toString();
                myNetwork.getOutput().write(input);
                myNetwork.getOutput().flush();
             myTextView.setText(input);
            }
        };
        myButton.setOnClickListener(myListener);

    }




}
