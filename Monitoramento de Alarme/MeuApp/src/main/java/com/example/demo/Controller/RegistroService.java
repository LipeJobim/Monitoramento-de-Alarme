package com.example.demo.Controller;

import java.util.List;

import org.springframework.stereotype.Service;

import com.example.demo.Models.Registro;

@Service
public class RegistroService {
	private final RegistroRepository registroRepository;

	
    public RegistroService(RegistroRepository registroRepository) {
        this.registroRepository = registroRepository;
    }

    public List<Registro> findAllRegistros() {
        return registroRepository.findAll();
    }

    public Registro saveRegistro(Registro registro) {
        return registroRepository.save(registro);
    }

    public List<Registro> listarTodosRegistros() {
        return registroRepository.findAll();
    }
}
