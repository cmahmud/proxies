# SyndProxy validated proxy pool

## Current pool

- Alive now: 496
- Gold now: 377
- HTTP: 109 alive / 61 gold
- HTTPS: 57 alive / 18 gold
- SOCKS4: 154 alive / 145 gold
- SOCKS5: 176 alive / 153 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38894
- Ever gold: 1293

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
