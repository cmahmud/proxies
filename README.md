# SyndProxy private pool

## Current pool

- Alive now: 939
- Gold now: 257
- HTTP: 343 alive / 27 gold
- HTTPS: 170 alive / 5 gold
- SOCKS4: 206 alive / 118 gold
- SOCKS5: 220 alive / 107 gold

## Historical pool

- Discovered: 99106
- Ever alive: 11777
- Ever gold: 389

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
