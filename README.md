# SyndProxy private pool

## Current pool

- Alive now: 753
- Gold now: 390
- HTTP: 208 alive / 86 gold
- HTTPS: 126 alive / 20 gold
- SOCKS4: 205 alive / 136 gold
- SOCKS5: 214 alive / 148 gold

## Historical pool

- Discovered: 155381
- Ever alive: 29191
- Ever gold: 1124

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
