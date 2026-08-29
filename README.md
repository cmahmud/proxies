# SyndProxy validated proxy pool

## Current pool

- Alive now: 358
- Gold now: 327
- HTTP: 36 alive / 22 gold
- HTTPS: 3 alive / 0 gold
- SOCKS4: 157 alive / 154 gold
- SOCKS5: 162 alive / 151 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43613
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
