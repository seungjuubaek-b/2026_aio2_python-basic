create extension if not exists "pgcrypto";

create table users (
  id uuid primary key default gen_random_uuid(),
  email text not null unique,
  username varchar(30) not null check(length(username) >= 2),
  created_at timestamptz not null default now()
);

INSERT INTO users (username, email) VALUES ('홍길동', 'f@example.com'),
('김길동', 'k@example.com'),
('이길동', 'l@example.com'),
('박길동', 'p@example.com'),
('조길동', 'j@example.com');