package com.example.demo.Controller;

import java.util.List;

import org.springframework.stereotype.Service;

import com.example.demo.Models.Vigilante;

@Service
public class VigilanteService {
	private final VigilanteRepository vigilanteRepository;

	public VigilanteService(VigilanteRepository vigilanteRepository) {
		this.vigilanteRepository = vigilanteRepository;
	}

	public List<Vigilante> listarTodosClientes() {
		return vigilanteRepository.findAll();
	}
}
