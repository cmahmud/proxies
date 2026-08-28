# SyndProxy validated proxy pool

## Current pool

- Alive now: 575
- Gold now: 419
- HTTP: 105 alive / 73 gold
- HTTPS: 106 alive / 22 gold
- SOCKS4: 182 alive / 156 gold
- SOCKS5: 182 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42508
- Ever gold: 1358

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
