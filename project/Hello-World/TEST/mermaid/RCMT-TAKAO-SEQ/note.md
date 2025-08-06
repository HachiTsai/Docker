# 語法筆記

## Mermaid流程圖語法

```mermaid
flowchart LR
    A[NOT-DB0049] -->|TRUE| C{判斷條件=<br>任一訊號為TRUE or FALSE}
    B[NOT-DI0093] -->|TRUE| C
    D[NOT-DI0001] -->|TRUE| C
    G[IN0101] -->|TRUE| C
    H[IN0102] -->|TRUE| C
    I[IN0103] -->|TRUE| C
    L[IN0108] -->|TRUE| C
    J[IN0152] -->|TRUE| C
    K[IN0131] -->|TRUE| C
    C -->|任一為 TRUE| E[MF01 = TRUE]
    C -->|任一為 FALSE| F[MF01 維持 FALSE]
```

## 顏色設定

style C3 fill:#fff,stroke:#333,stroke-width:1px,color:#ff0000
style C4 fill:#fff,stroke:#333,stroke-width:1px,color:#ff0000

## |TRUE|顏色設定

|"<font color='green'>TRUE</font>"|

|"<mark style='background-color:lightgreen'>TRUE</mark>"|

%%斜體+紅字%%
|"<font color='red' style='font-style:italic'>TRUE</font>"|

%%白底紅字%%
|<font color='red' style='background-color:white; padding:3px; border:1px solid red'>TRUE</font>|

%%白底紅字斜體粗體%%
|<font color='red' style='background-color:white; font-style:italic; font-weight:bold'>TRUE</font>|

|"<font color='red' style='background-color:white;font-style:italic; font-weight:bold'>NOT</font>"|

|"<font color='red' style='background-color:white;font-style:italic; font-weight:bold'>NOT</font>"| C1[TD0001 = TRUE<br>Time Count Start]
