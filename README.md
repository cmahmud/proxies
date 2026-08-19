# SyndProxy private pool

## Current pool

- Alive now: 1069
- Gold now: 343
- HTTP: 351 alive / 64 gold
- HTTPS: 287 alive / 17 gold
- SOCKS4: 206 alive / 112 gold
- SOCKS5: 225 alive / 150 gold

## Historical pool

- Discovered: 112027
- Ever alive: 16318
- Ever gold: 508

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
