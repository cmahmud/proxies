# SyndProxy private pool

## Current pool

- Alive now: 869
- Gold now: 415
- HTTP: 216 alive / 84 gold
- HTTPS: 185 alive / 20 gold
- SOCKS4: 230 alive / 156 gold
- SOCKS5: 238 alive / 155 gold

## Historical pool

- Discovered: 151674
- Ever alive: 27585
- Ever gold: 1100

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
