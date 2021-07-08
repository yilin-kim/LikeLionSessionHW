const $ulElement = document.querySelector("ul");

$ulElement.addEventListener("click", (event) => {
  const $target = event.target;
  //target이 close라는 class 가지고 있으면 부모를 없앰
  if ($target.classList.contains("close")) {
    const $parentTarget = $target.parentElement;
    $parentTarget.style.display = "none";
    // 원하는 위치 찾음
    console.dir($parentTarget);
    const deleteItem = $parentTarget.childNodes[1];
    deleteTodoList("todoList", deleteItem);
  }
  //checked라는 class 없으면 만들고 있으면 없게
  $target.classList.toggle("checked");
});

// $ulElement.addEvenetListener("click", (event) => {
//   const $target = event.target;
//   if ($target.classList.contains("close")) {
//     const $parentTarget = $target.parentElement;
//     $parentTarget.style.display = "none";
//     console.dir($parentTarget);
//     const deleteItem = $parentTarget.childNodes[1];
//   }
// });

function newElement() {
  const inputValue = document.getElementById("myInput").value;
  const $liElement = `
        <li>
            <span>${inputValue}</span>
            <span class="close">&#215;</span>
        </li>
    `;

  if (inputValue === "") {
    alert("You must write something!");
  } else {
    $ulElement.insertAdjacentHTML("beforeend", $liElement);
    addTodoList("todoList", inputValue);
  }
  document.getElementById("myInput").value = "";
}

//localStorage 확인 -> 데이터 있으면 -> li 객체들을 만들어주기
function init() {
  let key = "todoList";
  let myTodoList = getTodoList(key);
  if (myTodoList !== "") {
    for (let i = 0; i < myTodoList.length; i++) {
      $ulElement.insertAdjacentHTML(
        "beforeend",
        `<li>
          <span>${myTodoList[i]}</span>
      <span class="close">&#215;</span>
      </li>`
      );
    }
  }
}

//정답 코드
// function init() {
//   let todoList = getTodoList("todoList");
//   for (let i = 0; i < todoList.length; i++) {
//     $liElement = `
//             <li>
//                 <span>${todoList[i]}</span>
//                 <span class="close">&#215;</span>
//             </li>
//         `;
//     $ulElement.insertAdjacentHTML("beforeend", $liElement);
//   }
// }

//localStorage에 key값을 통해 key에 해당하는 value 리턴해주는 함수 아까 getItem
function getTodoList(key) {
  let localValue = localStorage.getItem(key);
  if (localValue) {
    return localValue.split(",");
  } else {
    return [];
  }
}

//key값을 통해 localStorage에 어떤 게 있는지 조회 -> 새로운 value를 배열로 return
//add누르면 addTodoList 실행
function addTodoList(key, value) {
  const todoList = getTodoList(key);
  // todoList.push(value);
  // localStorage.setItem(key,todoList);
  // *위의 2줄이 아닌 spread operator로 배열 추가하는 방법은
  return localStorage.setItem(key, [...todoList, value]);
}

//key값 통해 localStorage 정보 가져오기 -> array내에서 value에 해당 되는 값을 지운 새로운 배열 return
//x 누르면 deleteTodoList 실행
function deleteTodoList(key, value) {
  const todoList = getTodoList(key);
  // let newArray = [];
  // for (let i = 0; i < todoList.length; i++) {
  //   if (todoList.length !== value) {
  //     newArray.push(value);
  //   }
  // }
  // return newArray;

  return localStorage.setItem(
    key,
    todoList.filter((todo) => todo !== value)
  );
}

// Get the modal
let modal = document.getElementById("myModal");

// Get the button that opens the modal
let btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
let span = document.getElementsByClassName("close")[1];

// When the user clicks the button, open the modal
btn.onclick = function () {
  modal.style.display = "block";
};

// When the user clicks on <span> (x), close the modal
span.onclick = function () {
  modal.style.display = "none";
};

// When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
};

init();
