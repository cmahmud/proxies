# SyndProxy private pool

## Current pool

- Alive now: 1100
- Gold now: 350
- HTTP: 386 alive / 69 gold
- HTTPS: 279 alive / 17 gold
- SOCKS4: 199 alive / 109 gold
- SOCKS5: 236 alive / 155 gold

## Historical pool

- Discovered: 112027
- Ever alive: 16338
- Ever gold: 508

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
