# SyndProxy private pool

## Current pool

- Alive now: 1370
- Gold now: 432
- HTTP: 528 alive / 111 gold
- HTTPS: 301 alive / 25 gold
- SOCKS4: 223 alive / 141 gold
- SOCKS5: 318 alive / 155 gold

## Historical pool

- Discovered: 136248
- Ever alive: 22650
- Ever gold: 909

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
