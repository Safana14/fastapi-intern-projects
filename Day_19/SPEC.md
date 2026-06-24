# Sentiment Dashboard API Specification

## Overview

A REST API that stores user text entries and performs sentiment analysis using an AI model.

---

## Features

* User Registration
* User Login (JWT)
* Create Text Entry
* View Entries
* Delete Entry
* Sentiment Analysis
* Sentiment Reports
* Daily Trend Report

---

## Database Models

### User

| Field      | Type      |
| ---------- | --------- |
| id         | Integer   |
| username   | String    |
| email      | String    |
| password   | String    |
| created_at | Timestamp |

### Entry

| Field      | Type      |
| ---------- | --------- |
| id         | Integer   |
| user_id    | Integer   |
| text       | Text      |
| sentiment  | String    |
| score      | Float     |
| created_at | Timestamp |

---

## API Endpoints

### Auth

POST /register

Create User

POST /login

Generate JWT Token

---

### Entries

POST /entries

Create text entry

GET /entries

Get all entries

GET /entries/{id}

Get one entry

DELETE /entries/{id}

Delete entry

---

### Reports

GET /reports/summary

Sentiment counts

GET /reports/trends

Daily sentiment trends

---

## AI Feature

Hugging Face Sentiment Analysis Pipeline

Output:

* Positive
* Negative
* Neutral

---

## PostgreSQL Tables

users

entries

---

## Migration Tool

Alembic
