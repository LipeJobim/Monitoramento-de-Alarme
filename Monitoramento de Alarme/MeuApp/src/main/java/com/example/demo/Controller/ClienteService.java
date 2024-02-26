package com.example.demo.Controller;

import java.util.List;

import org.springframework.stereotype.Service;

import com.example.demo.Models.Cliente;

@Service
public class ClienteService {
	private final ClienteRepository clienteRepository;

	public ClienteService(ClienteRepository clienteRepository) {
		this.clienteRepository = clienteRepository;
	}

	public List<Cliente> listarTodosClientes() {
		return clienteRepository.findAll();
	}
}
