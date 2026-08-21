# SyndProxy private pool

## Current pool

- Alive now: 733
- Gold now: 391
- HTTP: 194 alive / 87 gold
- HTTPS: 122 alive / 21 gold
- SOCKS4: 209 alive / 135 gold
- SOCKS5: 208 alive / 148 gold

## Historical pool

- Discovered: 155381
- Ever alive: 29191
- Ever gold: 1124

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
