# SyndProxy private pool

## Current pool

- Alive now: 701
- Gold now: 345
- HTTP: 208 alive / 63 gold
- HTTPS: 99 alive / 15 gold
- SOCKS4: 201 alive / 135 gold
- SOCKS5: 193 alive / 132 gold

## Historical pool

- Discovered: 147177
- Ever alive: 25789
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
