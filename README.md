# SyndProxy validated proxy pool

## Current pool

- Alive now: 562
- Gold now: 410
- HTTP: 90 alive / 59 gold
- HTTPS: 95 alive / 22 gold
- SOCKS4: 182 alive / 163 gold
- SOCKS5: 195 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41495
- Ever gold: 1336

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
