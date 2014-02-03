drop table if exists documents;
create table documents (
  id integer primary key autoincrement,
  title text not null,
  author text not null
);

drop table if exists parts;
create table parts (
  id integer primary key autoincrement,
  documents_id integer not null,
  order integer not null,
  title text not null
);

drop table if exists parts_versions;
create table parts_versions (
  parts_id integer primary key not null,
  version integer not null,
  content text not null
);

drop table if exists users;
create table users (
  id integer primary key autoincrement,
  email text not null,
  password text not null
);
