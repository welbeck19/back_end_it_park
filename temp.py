# Mehmon haqida ma'lumotlar saqlanmoqda
guest_info = {
    "name": "Javlon",
    "room": 305,
    "nights": 3
}

# Oxirgi qo‘shilgan kalit-qiymat juftligi dictionary dan o‘chirilmoqda
removed_item = guest_info.popitem()

# O‘chirilgan juftlik (tuple shaklida) ekranga chiqarilmoqda
print("Removed:", removed_item)

# Yangilangan dictionary ekranga chiqarilmoqda
print("Updated:", guest_info)