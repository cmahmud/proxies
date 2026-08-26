# SyndProxy validated proxy pool

## Current pool

- Alive now: 470
- Gold now: 376
- HTTP: 96 alive / 63 gold
- HTTPS: 55 alive / 16 gold
- SOCKS4: 150 alive / 144 gold
- SOCKS5: 169 alive / 153 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38901
- Ever gold: 1293

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
