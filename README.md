# SyndProxy private pool

## Current pool

- Alive now: 1069
- Gold now: 524
- HTTP: 371 alive / 155 gold
- HTTPS: 279 alive / 87 gold
- SOCKS4: 219 alive / 148 gold
- SOCKS5: 200 alive / 134 gold

## Historical pool

- Discovered: 117177
- Ever alive: 17734
- Ever gold: 692

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
