# SyndProxy private pool

## Current pool

- Alive now: 677
- Gold now: 381
- HTTP: 170 alive / 68 gold
- HTTPS: 87 alive / 14 gold
- SOCKS4: 202 alive / 141 gold
- SOCKS5: 218 alive / 158 gold

## Historical pool

- Discovered: 147177
- Ever alive: 25790
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
