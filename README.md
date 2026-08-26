# SyndProxy validated proxy pool

## Current pool

- Alive now: 496
- Gold now: 373
- HTTP: 100 alive / 58 gold
- HTTPS: 67 alive / 17 gold
- SOCKS4: 154 alive / 144 gold
- SOCKS5: 175 alive / 154 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38892
- Ever gold: 1293

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
