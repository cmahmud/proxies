# SyndProxy validated proxy pool

## Current pool

- Alive now: 511
- Gold now: 377
- HTTP: 117 alive / 63 gold
- HTTPS: 68 alive / 17 gold
- SOCKS4: 152 alive / 144 gold
- SOCKS5: 174 alive / 153 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38822
- Ever gold: 1293

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
