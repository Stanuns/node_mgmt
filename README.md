# node 管理

## 1. 自主探索建图节点管理

### 1.1 自动探索建图模块当前状态反馈

- topic name: /auto_explore_mapping/state
- topic type: app_msgs/msg/AutoExploreMappingState
- 状态解释：

```bashrc
   -1:未初始化; 
   0:已初始化未开始;
   1:开始自动建图; 
   2:建图中; 
   3:建图完成并保存最终地图; 
   4:停止自动建图;
```

### 1.2 对自动探索建图模块进行控制

- 其他模块控制该模块的接口，比如语音模块控制该模块
- topic name: /auto_explore_mapping/trigger
- topic type: app_msgs/msg/AutoExploreMappingTrigger
- 状态解释：

```bashrc
  -1:未有动作; ### 该值是默认的，其他模块无需发此状态
  1:开始自动建图; ### 发此值之前/auto_explore_mapping/state是-1，
                ### 发完之后/auto_explore_mapping/state变成0，接着变成1，最后变成2.
  4:停止自动建图; ### 发此值之前/auto_explore_mapping/state是2， 
                ### 发完之后/auto_explore_mapping/state变成4，接着变成-1.
  5：保存当前地图; ###发此值之前/auto_explore_mapping/state是2.
```
