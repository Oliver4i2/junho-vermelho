CREATE DATABASE hemocentro_db;
USE hemocentro_db;







CREATE TABLE `estoque_sanguineo` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `tipo_sanguineo` VARCHAR(5) NOT NULL UNIQUE,
  `quantidade_bolsas` INT NOT NULL
);

-- Inserindo dados de exemplo para o Hemocentro de Brasília
INSERT INTO `estoque_sanguineo` (tipo_sanguineo, quantidade_bolsas) VALUES
('O+', 45),
('O-', 12),
('A+', 58),
('A-', 8),
('B+', 25),
('B-', 5),
('AB+', 15),
('AB-', 3);


-- Cria a tabela para armazenar os usuários
CREATE TABLE `usuarios` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `nome` VARCHAR(100) NOT NULL,
  `email` VARCHAR(100) NOT NULL UNIQUE,
  `senha_hash` VARCHAR(255) NOT NULL,
  `data_criacao` TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- Cria a tabela para armazenar os comentários
CREATE TABLE `comentarios` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `comentario_texto` TEXT NOT NULL,
  `data_postagem` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `usuario_id` INT NOT NULL,
  FOREIGN KEY (`usuario_id`) REFERENCES `usuarios`(`id`) ON DELETE CASCADE
);

-- Opcional: Inserir um comentário de exemplo para teste
-- Primeiro, insira um usuário para poder linkar o comentário a ele
-- A senha '123456' será convertida para um hash seguro pelo Python
-- INSERT INTO `usuarios` (nome, email, senha_hash) VALUES ('Usuário Teste', 'teste@email.com', 'hash_da_senha_aqui');
-- INSERT INTO `comentarios` (comentario_texto, usuario_id) VALUES ('Minha experiência doando sangue foi incrível! Recomendo a todos.', 1);
