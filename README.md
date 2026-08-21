# SyndProxy private pool

## Current pool

- Alive now: 720
- Gold now: 388
- HTTP: 191 alive / 84 gold
- HTTPS: 111 alive / 22 gold
- SOCKS4: 208 alive / 135 gold
- SOCKS5: 210 alive / 147 gold

## Historical pool

- Discovered: 155381
- Ever alive: 29191
- Ever gold: 1124

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
