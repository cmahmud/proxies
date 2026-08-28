# SyndProxy validated proxy pool

## Current pool

- Alive now: 575
- Gold now: 424
- HTTP: 104 alive / 74 gold
- HTTPS: 105 alive / 23 gold
- SOCKS4: 184 alive / 159 gold
- SOCKS5: 182 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42508
- Ever gold: 1358

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
