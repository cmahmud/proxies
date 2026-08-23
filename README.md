# SyndProxy validated proxy pool

## Current pool

- Alive now: 458
- Gold now: 363
- HTTP: 82 alive / 44 gold
- HTTPS: 27 alive / 8 gold
- SOCKS4: 170 alive / 155 gold
- SOCKS5: 179 alive / 156 gold

## Historical pool

- Discovered: 173056
- Ever alive: 33004
- Ever gold: 1222

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
