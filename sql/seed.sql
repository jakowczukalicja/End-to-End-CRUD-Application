insert into users(name, surname, email, password)
values
	('Alicja', 'Jakowczuk', 'alicja3@example.com', 'password1'),
  	('Julia', 'Radzimska', 'julka67@example.com', 'password67');

insert into picture (path, name)
values
  ('pink_flat_shoes.jpg', 'Pink flat shoes'),
  ('creamy_vintage_dress.jpg', 'Creamy vintage dress'),
  ('pink_dress.jpg', 'Pink dress'),
  ('white_vintage_dress.jpg', 'White vintage dress'),
  ('blue_midi_skirt.jpg', 'Blue tiered midi skirt'),
  ('denim_jeans.jpg', 'Light wash denim jeans'),
  ('linen_jacket.jpg', 'Beige linen suit jacket'),
  ('market_bag.jpg', 'Crochet market bag with fruit'),
  ('grey_totebag.jpg', 'Minimalist grey tote bag'),
  ('sunlit_dress.jpg', 'Sunlit vintage blue dress'),
  ('floral_bag.jpg', 'Floral shoulder bag on the door'),
  ('blue_tweed_dress.jpg', 'Powder blue tweed dress'),
  ('oversized_blazer.jpg', 'City chic oversized blazer'),
  ('black_patent_loafers.jpg', 'Black patent loafers'),
  ('blue_bag.jpg', 'Blue crochet tote bag'),
  ('light_blezer.jpg', 'Beige blazer with mini bag'),
  ('vintage2.jpg', 'Vintage beige patterned dress'),
  ('white_bag.jpg', 'White crochet net bag'),
  ('white_dress2.jpg', 'Beige lace collar dress'),
  ('green_tshirt.jpg', 'Mint green t-shirt flatlay'),
  ('grey_sweater.jpg', 'Grey wool sweater portrait'),
  ('jeans2.jpg', 'Blue denim jeans close-up'),
  ('orange_tshirt.jpg', 'Orange t-shirt on hanger'),
  ('pink_tshirt.jpg', 'Pink oversized t-shirt'),
  ('red_blouse.jpg', 'Red blouse portrait'),
  ('yellow_tshirt.jpg', 'Yellow t-shirt on rack');


insert into garments (category, size, colour, material, picture_id)
values
  ('shoes', '37',  'pink', 'synthetic patent',   1),
  ('dress',    'S',  'beige',  'embroidered lace',  2),
  ('dress',    'S',  'pink',  'satin',  3),
  ('dress',    'S',  'white',  'embroidered lace',  4), 
  ('skirt',  'M',  'blue',       'denim',        5), 
  ('jeans',  'M',  'blue', 'denim',        6), 
  ('blezer', 'M',  'beige',      'linen',        7), 
  ('bag',    'OS', 'brown',        'jute crochet', 8),
  ('bag',    'OS', 'grey',       'leather',      9), 
  ('dress',  'S',  'blue', 'linen',       10), 
  ('bag',    'OS', 'green',      'canvas',      11), 
  ('dress',  'S',  'blue', 'wool',       12),
  ('blazer', 'M',  'grey',       'wool',  13),
  ('shoes',  '38', 'black',      'synthetic patent', 14),
  ('bag',    'OS', 'blue',  'jute crochet',      15),
  ('blazer', 'M',  'beige', 'wool',             16),
  ('dress',  'S',  'beige', 'linen',            17),
  ('bag',    'OS', 'white', 'jute crochet',     18),
  ('dress',  'S',  'beige', 'embroidered lace', 19),
  ('tshirt',  'M', 'green',  'linen', 20),
  ('sweater', 'M', 'grey',   'wool',  21),
  ('jeans',   'M', 'blue',   'denim', 22),
  ('tshirt',  'M', 'orange', 'linen', 23),
  ('tshirt',  'M', 'pink',   'linen', 24),
  ('blouse',  'S', 'red',    'linen', 25),
  ('tshirt',  'M', 'yellow', 'linen', 26);

INSERT INTO garment_like (user_id, garment_id)
VALUES
  (1, 1), 
  (1, 2), 
  (1, 4),
  (1, 5),
  (1, 23),
  (1,26),
  (2, 19),
  (2, 23),
  (2, 25); 










