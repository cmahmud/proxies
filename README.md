# SyndProxy validated proxy pool

## Current pool

- Alive now: 473
- Gold now: 375
- HTTP: 99 alive / 61 gold
- HTTPS: 55 alive / 19 gold
- SOCKS4: 156 alive / 142 gold
- SOCKS5: 163 alive / 153 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38863
- Ever gold: 1293

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
