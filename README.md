# SyndProxy private pool

## Current pool

- Alive now: 674
- Gold now: 358
- HTTP: 179 alive / 74 gold
- HTTPS: 115 alive / 19 gold
- SOCKS4: 196 alive / 131 gold
- SOCKS5: 184 alive / 134 gold

## Historical pool

- Discovered: 147169
- Ever alive: 25781
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
