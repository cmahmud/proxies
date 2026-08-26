# SyndProxy validated proxy pool

## Current pool

- Alive now: 500
- Gold now: 373
- HTTP: 100 alive / 64 gold
- HTTPS: 64 alive / 15 gold
- SOCKS4: 157 alive / 143 gold
- SOCKS5: 179 alive / 151 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38808
- Ever gold: 1293

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
