# SyndProxy private pool

## Current pool

- Alive now: 771
- Gold now: 398
- HTTP: 188 alive / 79 gold
- HTTPS: 150 alive / 20 gold
- SOCKS4: 207 alive / 150 gold
- SOCKS5: 226 alive / 149 gold

## Historical pool

- Discovered: 151073
- Ever alive: 27511
- Ever gold: 1099

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
