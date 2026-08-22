# SyndProxy private pool

## Current pool

- Alive now: 945
- Gold now: 366
- HTTP: 294 alive / 78 gold
- HTTPS: 223 alive / 23 gold
- SOCKS4: 211 alive / 135 gold
- SOCKS5: 217 alive / 130 gold

## Historical pool

- Discovered: 165832
- Ever alive: 32358
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
