# SyndProxy validated proxy pool

## Current pool

- Alive now: 591
- Gold now: 439
- HTTP: 124 alive / 81 gold
- HTTPS: 92 alive / 27 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 201 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45460
- Ever gold: 1432

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
