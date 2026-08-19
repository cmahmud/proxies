# SyndProxy private pool

## Current pool

- Alive now: 1019
- Gold now: 554
- HTTP: 354 alive / 189 gold
- HTTPS: 269 alive / 99 gold
- SOCKS4: 177 alive / 121 gold
- SOCKS5: 219 alive / 145 gold

## Historical pool

- Discovered: 124835
- Ever alive: 19211
- Ever gold: 770

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
