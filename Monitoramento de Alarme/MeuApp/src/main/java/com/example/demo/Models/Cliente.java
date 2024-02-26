
package com.example.demo.Models;

import jakarta.persistence.*;
import java.time.LocalDate;
import java.time.LocalDateTime;

import com.fasterxml.jackson.annotation.JsonFormat;

@Entity
public class Cliente {
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private Long id;

	@Column(nullable = true, length = 100)
	private String nome;

	@Column(unique = true)
	private String email;

	@Column(unique = false)
	private String dataNascimento;

	@Column(unique = false)
	private String endereco;

	@Column(unique = false)
	private String telefone;

	@Column
	private String CEP;

	@Column(unique = true)
	private String CPF;

	@Column(nullable = false, updatable = false, columnDefinition = "TIMESTAMP DEFAULT CURRENT_TIMESTAMP")
	private LocalDateTime created_at;
	
	

	public Cliente() {
		super();
		// TODO Auto-generated constructor stub
	}

	public Cliente(Long id, String nome, String email, String dataNascimento, String endereco, String telefone,
			String CEP, String CPF) {
		super();
		this.id = id;
		this.nome = nome;
		this.email = email;
		this.dataNascimento = dataNascimento;
		this.endereco = endereco;
		this.telefone = telefone;
		this.CEP = CEP;
		this.CPF = CPF;
	}

	public Long getId() {
		return id;
	}

	public void setId(Long id) {
		this.id = id;
	}

	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public String getEmail() {
		return email;
	}

	public void setEmail(String email) {
		this.email = email;
	}

	public String getDataNascimento() {
		return dataNascimento;
	}

	public void setDataNascimento(String dataNascimento) {
		this.dataNascimento = dataNascimento;
	}

	public String getEndereco() {
		return endereco;
	}

	public void setEndereco(String endereco) {
		this.endereco = endereco;
	}

	public String getTelefone() {
		return telefone;
	}

	public void setTelefone(String telefone) {
		this.telefone = telefone;
	}

	public String getCEP() {
		return CEP;
	}

	public void setCEP(String CEP) {
		this.CEP = CEP;
	}

	public String getCPF() {
		return CPF;
	}

	public void setCPF(String CPF) {
		this.CPF = CPF;
	}

	public LocalDateTime getCreated_at() {
		return created_at;
	}

	@PrePersist
	public void prePersist() {
		created_at = LocalDateTime.now();
	}

	@Override
	public String toString() {
		return "Cliente [id=" + id + ", nome=" + nome + ", email=" + email + ", dataNascimento=" + dataNascimento
				+ ", endereco=" + endereco + ", telefone=" + telefone + ", CEP=" + CEP + ", CPF=" + CPF + ", getId()="
				+ getId() + ", getNome()=" + getNome() + ", getEmail()=" + getEmail() + ", getDataNascimento()="
				+ getDataNascimento() + ", getEndereco()=" + getEndereco() + ", getTelefone()=" + getTelefone()
				+ ", getCEP()=" + getCEP() + ", getCPF()=" + getCPF() + ", getClass()=" + getClass() + ", hashCode()="
				+ hashCode() + ", toString()=" + super.toString() + "]";
	}

}