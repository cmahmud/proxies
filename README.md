# SyndProxy private pool

## Current pool

- Alive now: 1031
- Gold now: 357
- HTTP: 387 alive / 90 gold
- HTTPS: 233 alive / 20 gold
- SOCKS4: 183 alive / 114 gold
- SOCKS5: 228 alive / 133 gold

## Historical pool

- Discovered: 153747
- Ever alive: 28814
- Ever gold: 1114

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
