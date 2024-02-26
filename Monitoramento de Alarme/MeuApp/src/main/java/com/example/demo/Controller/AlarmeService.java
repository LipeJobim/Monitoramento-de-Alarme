package com.example.demo.Controller;

import java.util.List;

import org.springframework.stereotype.Service;

import com.example.demo.Models.Alarme;

@Service
public class AlarmeService {
	private final AlarmeRepository alarmeRepository;

	public AlarmeService(AlarmeRepository alarmeRepository) {
		this.alarmeRepository = alarmeRepository;
	}

	public List<Alarme> listarTodosAlarmes() {
		return alarmeRepository.findAll();
	}
}
