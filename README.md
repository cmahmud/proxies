# SyndProxy validated proxy pool

## Current pool

- Alive now: 549
- Gold now: 418
- HTTP: 98 alive / 69 gold
- HTTPS: 99 alive / 19 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 182 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42542
- Ever gold: 1358

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
