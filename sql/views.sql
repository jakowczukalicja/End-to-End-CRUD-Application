create or replace view count_user_likes(user_id, name, surname, email, num_of_likes) as
select u.user_id, u.name, u.surname, u.email, count(gl.like_id) from users u 
left join garment_like gl on u.user_id = gl.user_id group by u.user_id
order by user_id;


create or replace view 
info_about_garments(garment_id, category, size, colour, material, name, path, num_of_likes) as
select g.garment_id, g.category, g.size, g.colour, g.material,
p."name" , p."path", count(gl.like_id)
from garments g inner join picture p  
on g.picture_id = p.picture_id 
left join garment_like gl 
on gl.garment_id = g.garment_id
group by g.garment_id, p.picture_id
order by g.garment_id;




