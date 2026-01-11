CREATE TABLE users (
  user_id   BIGSERIAL PRIMARY KEY,
  name      VARCHAR(50)  NOT NULL,
  surname   VARCHAR(50)  NOT NULL,
  email     VARCHAR(255) NOT NULL UNIQUE,
  password  VARCHAR(255) NOT NULL
);

CREATE TABLE picture (
  picture_id BIGSERIAL PRIMARY KEY,
  path       VARCHAR(500) NOT NULL,
  name       VARCHAR(100) NOT NULL
);

CREATE TABLE garments (
  garment_id BIGSERIAL PRIMARY KEY,
  category   VARCHAR(50)  NOT NULL,
  size       VARCHAR(20)  NOT NULL,
  colour     VARCHAR(30)  NOT NULL,
  material   VARCHAR(50)  NOT NULL,
  picture_id BIGINT NOT NULL UNIQUE,

  CONSTRAINT fk_garments_picture
    FOREIGN KEY (picture_id)
    REFERENCES picture(picture_id)
    ON DELETE RESTRICT
);

CREATE TABLE garment_like (
  like_id    BIGSERIAL PRIMARY KEY,
  user_id    BIGINT NOT NULL,
  garment_id BIGINT NOT NULL,
  
  CONSTRAINT fk_like_user
    FOREIGN KEY (user_id)
    REFERENCES users(user_id)
    ON DELETE CASCADE,

  CONSTRAINT fk_like_garment
    FOREIGN KEY (garment_id)
    REFERENCES garments(garment_id)
    ON DELETE CASCADE,

  CONSTRAINT uq_like_once
    UNIQUE (user_id, garment_id)
);
