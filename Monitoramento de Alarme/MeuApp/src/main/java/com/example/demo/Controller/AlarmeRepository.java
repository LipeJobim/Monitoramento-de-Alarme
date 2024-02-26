package com.example.demo.Controller;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.http.ResponseEntity;

import com.example.demo.Models.Alarme;

public interface AlarmeRepository extends JpaRepository<Alarme, Long>{

	List<Alarme> findAll();

	Alarme deleteAllById(Long id);

	ResponseEntity<Alarme> save(String status);
}
