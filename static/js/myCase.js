// 获取项目列表
var projectListInit = function (_cmbProject) {
	var cmbProject = document.getElementById(_cmbProject);
	var options = "";

	//创建下拉选项
	function cmbAddOption(cmb, project_obj) {
		console.log(project_obj);
		var option = document.createElement("option");
		option.innerHTML = project_obj.name;
		option.value = project_obj.id;
		cmb.options.add(option);
		$('#'+_cmbProject).selectpicker('refresh');
	}

	function getProjectListInfo() {
		// 获取某个项目的信息
		$.get("/project/get_project_list/", {}, function (resp) {
			if (resp.success === "true") {
				let dataList = resp.data;
				for (let i = 0; i < dataList.length; i++) {
					cmbAddOption(cmbProject, dataList[i]);
				}
			} else {
				window.alert(resp.message);
			}
		});
	}

	// 调用getProjectListInfo函数
	getProjectListInfo();

};

// 获取某一个项目的模块列表
var moduleListInit = function (_cmbModule, pid) {
	var cmbModule = document.getElementById(_cmbModule);
	var options = "";

	//创建下拉选项
	function cmbAddOption(cmb, module_obj) {
		console.log(module_obj);
		var option = document.createElement("option");
		option.innerHTML = module_obj.name;
		option.value = module_obj.id;
		cmb.options.add(option);
		$('#'+_cmbModule).selectpicker('refresh');
	}

	function getModuleListInfo() {
		// 获取模块的信息
		$.post("/module/get_module_list/", {
		    "pid": pid
        }, function (resp) {
			if (resp.success === "true") {
				let dataList = resp.data;
				$('#'+_cmbModule).empty();
				for (let i = 0; i < dataList.length; i++) {
					cmbAddOption(cmbModule, dataList[i]);
				}
			} else {
				window.alert(resp.message);
			}
		});
	}

	getModuleListInfo();

};

//获取用例信息
var testCaseInit = function () {
	let pathname = document.location.pathname;
	let cid = pathname.split("/")[3];
	$.post("/testcase/get_case_info/", {
                cid: cid
            },
            function (resp, status) {
                document.querySelector("#req_url").value = resp.data.url;
                document.querySelector("#case_name").value = resp.data.name;
            }
		)
};