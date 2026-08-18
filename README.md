# SyndProxy private pool

## Current pool

- Alive now: 999
- Gold now: 301
- HTTP: 385 alive / 29 gold
- HTTPS: 198 alive / 5 gold
- SOCKS4: 210 alive / 141 gold
- SOCKS5: 206 alive / 126 gold

## Historical pool

- Discovered: 102848
- Ever alive: 13392
- Ever gold: 415

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
