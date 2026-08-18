# SyndProxy private pool

## Current pool

- Alive now: 947
- Gold now: 260
- HTTP: 348 alive / 29 gold
- HTTPS: 170 alive / 6 gold
- SOCKS4: 210 alive / 118 gold
- SOCKS5: 219 alive / 107 gold

## Historical pool

- Discovered: 99106
- Ever alive: 11778
- Ever gold: 389

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
