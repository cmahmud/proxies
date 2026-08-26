# SyndProxy validated proxy pool

## Current pool

- Alive now: 501
- Gold now: 372
- HTTP: 107 alive / 60 gold
- HTTPS: 68 alive / 15 gold
- SOCKS4: 156 alive / 145 gold
- SOCKS5: 170 alive / 152 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38899
- Ever gold: 1293

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
