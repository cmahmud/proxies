# SyndProxy validated proxy pool

## Current pool

- Alive now: 568
- Gold now: 413
- HTTP: 99 alive / 71 gold
- HTTPS: 121 alive / 22 gold
- SOCKS4: 168 alive / 157 gold
- SOCKS5: 180 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41900
- Ever gold: 1344

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
