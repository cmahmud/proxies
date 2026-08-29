# SyndProxy validated proxy pool

## Current pool

- Alive now: 367
- Gold now: 344
- HTTP: 40 alive / 29 gold
- HTTPS: 5 alive / 1 gold
- SOCKS4: 157 alive / 156 gold
- SOCKS5: 165 alive / 158 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43613
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
