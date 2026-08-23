# SyndProxy validated proxy pool

## Current pool

- Alive now: 521
- Gold now: 340
- HTTP: 89 alive / 31 gold
- HTTPS: 50 alive / 8 gold
- SOCKS4: 180 alive / 148 gold
- SOCKS5: 202 alive / 153 gold

## Historical pool

- Discovered: 172299
- Ever alive: 32956
- Ever gold: 1217

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
