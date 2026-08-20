# SyndProxy private pool

## Current pool

- Alive now: 909
- Gold now: 410
- HTTP: 240 alive / 89 gold
- HTTPS: 249 alive / 18 gold
- SOCKS4: 204 alive / 151 gold
- SOCKS5: 216 alive / 152 gold

## Historical pool

- Discovered: 151674
- Ever alive: 27548
- Ever gold: 1099

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
