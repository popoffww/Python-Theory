#Вывести квадраты чисел

def square(*args)

  args.map { |arg| puts arg ** 2}
    
end

square(1, 2, 3, 4, 5)

puts("=====")

def square(*args)

  args.each do |arg|
    puts arg * arg

  end
end

square(1, 2, 3, 4, 5)
