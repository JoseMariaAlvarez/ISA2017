package com.example.juanignacio.controlinr;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;

/**
 * Created by Juan Ignacio on 25/04/2017.
 */
public class MenuGuias extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_menuguias);
        Button boton = (Button) findViewById(R.id.btPaciente);
        Button boton2 = (Button) findViewById(R.id.btProfesional);
        Button boton3 = (Button) findViewById(R.id.btEmergencia);

    }
    public void abrirPaciente(View v){
        Intent intent =new Intent(this, GuiaPaciente.class);
        startActivity(intent);
    }
    public void abrirProfesional(View v){
        Intent intent =new Intent(this, GuiaProfesional.class);
        startActivity(intent);
    }
    public void abrirEmergencia(View v){
        Intent intent =new Intent(this, GuiaEmergencia.class);
        startActivity(intent);
    }
}