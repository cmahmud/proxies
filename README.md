# SyndProxy private pool

## Current pool

- Alive now: 1463
- Gold now: 556
- HTTP: 558 alive / 178 gold
- HTTPS: 353 alive / 85 gold
- SOCKS4: 223 alive / 139 gold
- SOCKS5: 329 alive / 154 gold

## Historical pool

- Discovered: 136248
- Ever alive: 22708
- Ever gold: 909

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
