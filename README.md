# SyndProxy private pool

## Current pool

- Alive now: 950
- Gold now: 390
- HTTP: 293 alive / 82 gold
- HTTPS: 208 alive / 28 gold
- SOCKS4: 195 alive / 122 gold
- SOCKS5: 254 alive / 158 gold

## Historical pool

- Discovered: 164916
- Ever alive: 32141
- Ever gold: 1171

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
