# SyndProxy validated proxy pool

## Current pool

- Alive now: 396
- Gold now: 316
- HTTP: 88 alive / 63 gold
- HTTPS: 40 alive / 19 gold
- SOCKS4: 119 alive / 104 gold
- SOCKS5: 149 alive / 130 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49494
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
