# SyndProxy validated proxy pool

## Current pool

- Alive now: 462
- Gold now: 378
- HTTP: 93 alive / 63 gold
- HTTPS: 50 alive / 17 gold
- SOCKS4: 152 alive / 145 gold
- SOCKS5: 167 alive / 153 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38902
- Ever gold: 1293

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
