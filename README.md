# SyndProxy validated proxy pool

## Current pool

- Alive now: 366
- Gold now: 294
- HTTP: 37 alive / 25 gold
- HTTPS: 5 alive / 1 gold
- SOCKS4: 158 alive / 135 gold
- SOCKS5: 166 alive / 133 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43613
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
