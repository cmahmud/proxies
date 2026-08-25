# SyndProxy validated proxy pool

## Current pool

- Alive now: 505
- Gold now: 416
- HTTP: 92 alive / 67 gold
- HTTPS: 67 alive / 20 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 173 alive / 168 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37096
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
