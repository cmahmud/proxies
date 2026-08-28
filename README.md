# SyndProxy validated proxy pool

## Current pool

- Alive now: 548
- Gold now: 414
- HTTP: 96 alive / 67 gold
- HTTPS: 99 alive / 19 gold
- SOCKS4: 171 alive / 160 gold
- SOCKS5: 182 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42541
- Ever gold: 1358

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
