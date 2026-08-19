# SyndProxy private pool

## Current pool

- Alive now: 1024
- Gold now: 488
- HTTP: 383 alive / 152 gold
- HTTPS: 267 alive / 87 gold
- SOCKS4: 179 alive / 115 gold
- SOCKS5: 195 alive / 134 gold

## Historical pool

- Discovered: 117177
- Ever alive: 17741
- Ever gold: 692

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
