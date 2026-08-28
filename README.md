# SyndProxy validated proxy pool

## Current pool

- Alive now: 574
- Gold now: 414
- HTTP: 96 alive / 68 gold
- HTTPS: 116 alive / 21 gold
- SOCKS4: 180 alive / 160 gold
- SOCKS5: 182 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42600
- Ever gold: 1358

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
