# SyndProxy validated proxy pool

## Current pool

- Alive now: 525
- Gold now: 343
- HTTP: 88 alive / 31 gold
- HTTPS: 61 alive / 8 gold
- SOCKS4: 177 alive / 149 gold
- SOCKS5: 199 alive / 155 gold

## Historical pool

- Discovered: 172299
- Ever alive: 32956
- Ever gold: 1217

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
