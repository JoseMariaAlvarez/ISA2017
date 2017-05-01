package com.example.juanignacio.controlinr;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Button boton = (Button) findViewById(R.id.btGuias);
    }

    /** Es llamado cuando el usuario hace click sobre el botón Guías */
    public void abrirGuias(View v) {
        Intent intent =new Intent(this, MenuGuias.class);
        startActivity(intent);
    }
}
