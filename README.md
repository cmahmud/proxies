# SyndProxy validated proxy pool

## Current pool

- Alive now: 575
- Gold now: 426
- HTTP: 102 alive / 77 gold
- HTTPS: 120 alive / 23 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 184 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42131
- Ever gold: 1351

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
