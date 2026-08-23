# SyndProxy validated proxy pool

## Current pool

- Alive now: 522
- Gold now: 348
- HTTP: 113 alive / 32 gold
- HTTPS: 31 alive / 8 gold
- SOCKS4: 179 alive / 151 gold
- SOCKS5: 199 alive / 157 gold

## Historical pool

- Discovered: 172299
- Ever alive: 32956
- Ever gold: 1217

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
