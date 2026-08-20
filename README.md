# SyndProxy private pool

## Current pool

- Alive now: 768
- Gold now: 395
- HTTP: 188 alive / 72 gold
- HTTPS: 152 alive / 19 gold
- SOCKS4: 214 alive / 155 gold
- SOCKS5: 214 alive / 149 gold

## Historical pool

- Discovered: 149502
- Ever alive: 26741
- Ever gold: 1087

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
