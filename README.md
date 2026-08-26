# SyndProxy validated proxy pool

## Current pool

- Alive now: 481
- Gold now: 370
- HTTP: 91 alive / 61 gold
- HTTPS: 68 alive / 14 gold
- SOCKS4: 152 alive / 144 gold
- SOCKS5: 170 alive / 151 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38837
- Ever gold: 1293

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
