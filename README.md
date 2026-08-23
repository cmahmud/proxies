# SyndProxy validated proxy pool

## Current pool

- Alive now: 321
- Gold now: 203
- HTTP: 100 alive / 40 gold
- HTTPS: 31 alive / 6 gold
- SOCKS4: 83 alive / 68 gold
- SOCKS5: 107 alive / 89 gold

## Historical pool

- Discovered: 170533
- Ever alive: 32764
- Ever gold: 1209

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
