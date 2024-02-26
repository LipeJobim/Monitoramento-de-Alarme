package com.example.demo.Controller;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.example.demo.Models.Vigilante;

@Repository
public interface VigilanteRepository extends JpaRepository<Vigilante, Long>{

	List<Vigilante> findAll();

}
