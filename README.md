# SyndProxy private pool

## Current pool

- Alive now: 1061
- Gold now: 350
- HTTP: 360 alive / 68 gold
- HTTPS: 263 alive / 17 gold
- SOCKS4: 198 alive / 110 gold
- SOCKS5: 240 alive / 155 gold

## Historical pool

- Discovered: 112027
- Ever alive: 16326
- Ever gold: 508

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
