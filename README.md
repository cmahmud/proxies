# SyndProxy validated proxy pool

## Current pool

- Alive now: 545
- Gold now: 427
- HTTP: 106 alive / 78 gold
- HTTPS: 79 alive / 21 gold
- SOCKS4: 182 alive / 162 gold
- SOCKS5: 178 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37908
- Ever gold: 1288

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
