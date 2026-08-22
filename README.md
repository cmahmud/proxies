# SyndProxy private pool

## Current pool

- Alive now: 916
- Gold now: 363
- HTTP: 301 alive / 75 gold
- HTTPS: 190 alive / 25 gold
- SOCKS4: 200 alive / 133 gold
- SOCKS5: 225 alive / 130 gold

## Historical pool

- Discovered: 165832
- Ever alive: 32355
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
