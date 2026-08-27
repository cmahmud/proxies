# SyndProxy validated proxy pool

## Current pool

- Alive now: 574
- Gold now: 413
- HTTP: 96 alive / 60 gold
- HTTPS: 99 alive / 23 gold
- SOCKS4: 179 alive / 164 gold
- SOCKS5: 200 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41490
- Ever gold: 1336

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
