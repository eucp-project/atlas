(window.webpackJsonp=window.webpackJsonp||[]).push([[7,3],{234:function(t,e,n){"use strict";n.r(e);var r={props:{text:{type:String,required:!0},target:{type:String,required:!1,default:""}}},o=n(38),component=Object(o.a)(r,(function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",[n("NuxtLink",{attrs:{to:t.target}},[n("button",{staticClass:"bg-transparent hover:bg-gray-500 active:bg-gray-700\n      text-gray-700 font-semibold hover:text-white py-2 px-4 border\n      border-gray-500 hover:border-transparent rounded-full\n      focus:outline-none"},[t._v("\n      "+t._s(t.text)+"\n    ")])])],1)}),[],!1,null,null,null);e.default=component.exports;installComponents(component,{Button:n(234).default})},240:function(t,e,n){t.exports=n.p+"img/ccby_logo.10f2b34.png"},526:function(t,e,n){"use strict";n.r(e);var r=[function(){var t=this.$createElement,e=this._self._c||t;return e("a",{attrs:{href:"https://creativecommons.org/licenses/by/4.0/"}},[e("img",{staticClass:"absolute bottom-8 right-1/3",attrs:{src:n(240),alt:"CC BY Logo"}})])}],o={data:function(){return{maps:[{path:n(238)}]}},methods:{clone:function(t){return JSON.parse(JSON.stringify(t))},getLetter:function(t){return String.fromCharCode(65+t)}}},l=n(38),component=Object(l.a)(o,(function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"flex flex-col items-center h-full max-h-full"},[n("div",{staticClass:"flex flex-col justify-start gap-1"},t._l(t.maps,(function(map,i){return n("div",{key:i},[n("MapSelector",{model:{value:map.path,callback:function(e){t.$set(map,"path",e)},expression:"map.path"}}),t._v(" "),1!=t.maps.length?n("button",{staticClass:"mx-4",on:{click:function(e){return t.maps.splice(i,1)}}},[n("font-awesome-icon",{attrs:{icon:["fas","trash"]}})],1):t._e(),t._v(" "),i===t.maps.length-1?n("button",{staticClass:"mx-4",on:{click:function(e){t.maps.push(t.clone(map))}}},[n("font-awesome-icon",{attrs:{icon:["fas","plus"]}})],1):t._e()],1)})),0),t._v(" "),n("div",{staticClass:"flex flex-grow w-full"},t._l(t.maps,(function(map,e){return n("span",{key:e,staticClass:"bg-center bg-no-repeat bg-contain flex-grow",style:{backgroundImage:"url("+map.path+")"}},[n("p",{staticClass:"absolute bottom-8 left-1/4 text-center text-sm"},[t._v("\n        Figures can be used under a\n        "),n("a",{attrs:{href:"https://creativecommons.org/licenses/by/4.0/"}},[t._v(" CC-BY 4.0 licence.\n        ")]),t._v("\n        see "),n("NuxtLink",{staticClass:"hover:text-blue-400 underline",attrs:{to:"/about"}},[t._v("ABOUT")]),t._v(" on how to cite the Atlas.\n      ")],1),t._v(" "),t._m(0,!0)])})),0)])}),r,!1,null,null,null);e.default=component.exports;installComponents(component,{MapSelector:n(522).default,Button:n(234).default})}}]);