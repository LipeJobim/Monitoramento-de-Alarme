package com.example.demo.Controller;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;

import com.example.demo.Models.Registro;

public interface RegistroRepository extends JpaRepository<Registro, Long>{
	
	List<Registro> findByDescricao(String descricao);


}
