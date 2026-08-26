# SyndProxy validated proxy pool

## Current pool

- Alive now: 553
- Gold now: 414
- HTTP: 101 alive / 67 gold
- HTTPS: 100 alive / 19 gold
- SOCKS4: 178 alive / 162 gold
- SOCKS5: 174 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37834
- Ever gold: 1288

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
