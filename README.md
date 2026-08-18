# SyndProxy private pool

## Current pool

- Alive now: 944
- Gold now: 349
- HTTP: 299 alive / 51 gold
- HTTPS: 187 alive / 13 gold
- SOCKS4: 215 alive / 135 gold
- SOCKS5: 243 alive / 150 gold

## Historical pool

- Discovered: 107131
- Ever alive: 14900
- Ever gold: 478

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
