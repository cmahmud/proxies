# SyndProxy validated proxy pool

## Current pool

- Alive now: 500
- Gold now: 376
- HTTP: 104 alive / 60 gold
- HTTPS: 64 alive / 18 gold
- SOCKS4: 154 alive / 145 gold
- SOCKS5: 178 alive / 153 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38892
- Ever gold: 1293

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
