# SyndProxy private pool

## Current pool

- Alive now: 672
- Gold now: 375
- HTTP: 170 alive / 69 gold
- HTTPS: 89 alive / 13 gold
- SOCKS4: 198 alive / 138 gold
- SOCKS5: 215 alive / 155 gold

## Historical pool

- Discovered: 147177
- Ever alive: 25800
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
