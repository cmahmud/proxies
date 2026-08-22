# SyndProxy private pool

## Current pool

- Alive now: 1041
- Gold now: 410
- HTTP: 314 alive / 82 gold
- HTTPS: 253 alive / 25 gold
- SOCKS4: 222 alive / 151 gold
- SOCKS5: 252 alive / 152 gold

## Historical pool

- Discovered: 165751
- Ever alive: 32292
- Ever gold: 1177

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
