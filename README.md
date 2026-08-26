# SyndProxy validated proxy pool

## Current pool

- Alive now: 562
- Gold now: 426
- HTTP: 108 alive / 77 gold
- HTTPS: 95 alive / 21 gold
- SOCKS4: 182 alive / 164 gold
- SOCKS5: 177 alive / 164 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37885
- Ever gold: 1288

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
