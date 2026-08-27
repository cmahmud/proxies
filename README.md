# SyndProxy validated proxy pool

## Current pool

- Alive now: 574
- Gold now: 417
- HTTP: 107 alive / 77 gold
- HTTPS: 114 alive / 17 gold
- SOCKS4: 173 alive / 158 gold
- SOCKS5: 180 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42072
- Ever gold: 1349

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
