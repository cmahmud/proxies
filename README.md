# SyndProxy private pool

## Current pool

- Alive now: 576
- Gold now: 230
- HTTP: 141 alive / 29 gold
- HTTPS: 70 alive / 8 gold
- SOCKS4: 168 alive / 111 gold
- SOCKS5: 197 alive / 82 gold

## Historical pool

- Discovered: 91695
- Ever alive: 8361
- Ever gold: 354

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
