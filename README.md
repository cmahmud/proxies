# SyndProxy validated proxy pool

## Current pool

- Alive now: 509
- Gold now: 375
- HTTP: 109 alive / 61 gold
- HTTPS: 70 alive / 17 gold
- SOCKS4: 156 alive / 145 gold
- SOCKS5: 174 alive / 152 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38899
- Ever gold: 1293

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
