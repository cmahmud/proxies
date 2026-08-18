# SyndProxy private pool

## Current pool

- Alive now: 938
- Gold now: 349
- HTTP: 290 alive / 51 gold
- HTTPS: 186 alive / 13 gold
- SOCKS4: 222 alive / 135 gold
- SOCKS5: 240 alive / 150 gold

## Historical pool

- Discovered: 107131
- Ever alive: 14900
- Ever gold: 478

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
