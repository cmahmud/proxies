# SyndProxy private pool

## Current pool

- Alive now: 790
- Gold now: 408
- HTTP: 228 alive / 89 gold
- HTTPS: 106 alive / 18 gold
- SOCKS4: 218 alive / 150 gold
- SOCKS5: 238 alive / 151 gold

## Historical pool

- Discovered: 155739
- Ever alive: 29280
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
