# SyndProxy validated proxy pool

## Current pool

- Alive now: 457
- Gold now: 370
- HTTP: 90 alive / 62 gold
- HTTPS: 51 alive / 16 gold
- SOCKS4: 150 alive / 142 gold
- SOCKS5: 166 alive / 150 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38872
- Ever gold: 1293

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
