# SyndProxy validated proxy pool

## Current pool

- Alive now: 496
- Gold now: 377
- HTTP: 112 alive / 64 gold
- HTTPS: 46 alive / 12 gold
- SOCKS4: 163 alive / 152 gold
- SOCKS5: 175 alive / 149 gold

## Historical pool

- Discovered: 176962
- Ever alive: 33251
- Ever gold: 1232

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
