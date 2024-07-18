PRAGMA foreign_keys = OFF;
DROP TABLE IF EXISTS task_character;
SELECT * FROM tasks_character WHERE character_type_id NOT IN (SELECT id FROM tasks_charactertype);

DROP TABLE IF EXISTS tasks_attribute;
DROP TABLE IF EXISTS tasks_character;
DROP TABLE IF EXISTS tasks_characterattribute;
DROP TABLE IF EXISTS tasks_archtype;
DROP TABLE IF EXISTS tasks_todo;
DROP TABLE IF EXISTS tasks_user;
DROP TABLE IF EXISTS tasks_weapon;
DROP TABLE IF EXISTS tasks_specialability;
DROP TABLE IF EXISTS tasks_skill;
DROP TABLE IF EXISTS tasks_possession;
DROP TABLE IF EXISTS tasks_note;
DROP TABLE IF EXISTS tasks_health;
DROP TABLE IF EXISTS tasks_forceskill;
DROP TABLE IF EXISTS tasks_force;
DROP TABLE IF EXISTS tasks_experience;
DROP TABLE IF EXISTS tasks_equipment;
DROP TABLE IF EXISTS tasks_edgeorflaw;
DROP TABLE IF EXISTS tasks_archetypeattribute;
DROP TABLE IF EXISTS tasks_armor;


SELECT COUNT(*) FROM tasks_equipment;

DELETE FROM tasks_equipment;
DELETE FROM sqlite_sequence WHERE name='tasks_equipment';

