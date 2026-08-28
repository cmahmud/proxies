# SyndProxy validated proxy pool

## Current pool

- Alive now: 572
- Gold now: 414
- HTTP: 113 alive / 69 gold
- HTTPS: 107 alive / 17 gold
- SOCKS4: 168 alive / 161 gold
- SOCKS5: 184 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42542
- Ever gold: 1358

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
