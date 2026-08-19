# SyndProxy private pool

## Current pool

- Alive now: 976
- Gold now: 353
- HTTP: 314 alive / 75 gold
- HTTPS: 217 alive / 9 gold
- SOCKS4: 215 alive / 124 gold
- SOCKS5: 230 alive / 145 gold

## Historical pool

- Discovered: 129290
- Ever alive: 20284
- Ever gold: 864

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
