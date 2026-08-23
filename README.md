# SyndProxy validated proxy pool

## Current pool

- Alive now: 541
- Gold now: 345
- HTTP: 95 alive / 30 gold
- HTTPS: 51 alive / 8 gold
- SOCKS4: 187 alive / 151 gold
- SOCKS5: 208 alive / 156 gold

## Historical pool

- Discovered: 172299
- Ever alive: 32956
- Ever gold: 1217

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
