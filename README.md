# SyndProxy private pool

## Current pool

- Alive now: 1429
- Gold now: 564
- HTTP: 488 alive / 189 gold
- HTTPS: 348 alive / 97 gold
- SOCKS4: 226 alive / 147 gold
- SOCKS5: 367 alive / 131 gold

## Historical pool

- Discovered: 140465
- Ever alive: 23624
- Ever gold: 924

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
