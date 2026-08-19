# SyndProxy private pool

## Current pool

- Alive now: 925
- Gold now: 342
- HTTP: 297 alive / 68 gold
- HTTPS: 199 alive / 16 gold
- SOCKS4: 201 alive / 112 gold
- SOCKS5: 228 alive / 146 gold

## Historical pool

- Discovered: 111011
- Ever alive: 16180
- Ever gold: 508

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
