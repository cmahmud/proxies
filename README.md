# SyndProxy private pool

## Current pool

- Alive now: 1000
- Gold now: 359
- HTTP: 334 alive / 60 gold
- HTTPS: 201 alive / 14 gold
- SOCKS4: 237 alive / 148 gold
- SOCKS5: 228 alive / 137 gold

## Historical pool

- Discovered: 107156
- Ever alive: 15139
- Ever gold: 484

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
