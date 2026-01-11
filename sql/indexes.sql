create index if not exists
idx_garment_like_user_id 
on garment_like (user_id);

create index if not exists
idx_garment_like_garment_id
on garment_like (garment_id);

create index if not exists
idx_garments_picture_id
on garments (picture_id);

