# SyndProxy private pool

## Current pool

- Alive now: 914
- Gold now: 348
- HTTP: 291 alive / 52 gold
- HTTPS: 179 alive / 12 gold
- SOCKS4: 214 alive / 134 gold
- SOCKS5: 230 alive / 150 gold

## Historical pool

- Discovered: 107131
- Ever alive: 14910
- Ever gold: 478

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
