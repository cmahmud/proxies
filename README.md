# SyndProxy validated proxy pool

## Current pool

- Alive now: 475
- Gold now: 379
- HTTP: 77 alive / 55 gold
- HTTPS: 63 alive / 15 gold
- SOCKS4: 166 alive / 156 gold
- SOCKS5: 169 alive / 153 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43486
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
