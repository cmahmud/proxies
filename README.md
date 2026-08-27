# SyndProxy validated proxy pool

## Current pool

- Alive now: 659
- Gold now: 407
- HTTP: 106 alive / 67 gold
- HTTPS: 183 alive / 19 gold
- SOCKS4: 179 alive / 156 gold
- SOCKS5: 191 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40610
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
