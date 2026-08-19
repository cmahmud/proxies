# SyndProxy private pool

## Current pool

- Alive now: 1063
- Gold now: 349
- HTTP: 367 alive / 67 gold
- HTTPS: 258 alive / 17 gold
- SOCKS4: 200 alive / 110 gold
- SOCKS5: 238 alive / 155 gold

## Historical pool

- Discovered: 112027
- Ever alive: 16324
- Ever gold: 508

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
