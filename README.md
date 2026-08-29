# SyndProxy validated proxy pool

## Current pool

- Alive now: 360
- Gold now: 336
- HTTP: 36 alive / 24 gold
- HTTPS: 2 alive / 0 gold
- SOCKS4: 159 alive / 156 gold
- SOCKS5: 163 alive / 156 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43613
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
