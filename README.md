# SyndProxy private pool

## Current pool

- Alive now: 785
- Gold now: 240
- HTTP: 332 alive / 29 gold
- HTTPS: 90 alive / 4 gold
- SOCKS4: 170 alive / 113 gold
- SOCKS5: 193 alive / 94 gold

## Historical pool

- Discovered: 95381
- Ever alive: 10428
- Ever gold: 377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
