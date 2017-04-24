function students(){

  var students =
  [
    {first_name: 'Michael', last_name: 'Jordan'},
    {first_name: 'John', last_name: 'Rosales'},
    {first_name: 'Mark', last_name: 'Guillen'},
    {first_name: 'KB', last_name: 'Tonel'}
  ]

  for(var name in students)
  {
    console.log(students[name].first_name, students[name].last_name);
  }
}

function studsAndInts(){

  var users =
  {
    'Students':
    [
      {first_name: 'Michael', last_name: 'Jordan'},
      {first_name: 'John', last_name: 'Rosales'},
      {first_name: 'Mark', last_name: 'Guillen'},
      {first_name: 'KB', last_name: 'Tonel'}
    ],
    'Instructors':
    [
      {first_name: 'Michael', last_name: 'Choi'},
      {first_name: 'Martin', last_name: 'Puryear'}
    ]
  }
  var studs = users.Students;
  var ints = users.Instructors;

    console.log("Students");
    for (var name in studs)
    {
      console.log((parseInt(name)+1)+" "+studs[name].first_name+ " "+studs[name].last_name+" - "+(studs[name].first_name.length+studs[name].last_name.length));
    }
    console.log("Instructors");
    for (var name2 in ints)
    {
      console.log((parseInt(name2)+1)+" "+studs[name2].first_name+" " +studs[name2].last_name+" - "+(ints[name2].first_name.length+ints[name2].last_name.length));
    }
}
