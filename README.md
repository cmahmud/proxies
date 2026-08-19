# SyndProxy private pool

## Current pool

- Alive now: 1293
- Gold now: 402
- HTTP: 434 alive / 91 gold
- HTTPS: 324 alive / 20 gold
- SOCKS4: 238 alive / 139 gold
- SOCKS5: 297 alive / 152 gold

## Historical pool

- Discovered: 135758
- Ever alive: 22202
- Ever gold: 893

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
