# SyndProxy private pool

## Current pool

- Alive now: 971
- Gold now: 407
- HTTP: 336 alive / 79 gold
- HTTPS: 198 alive / 21 gold
- SOCKS4: 211 alive / 152 gold
- SOCKS5: 226 alive / 155 gold

## Historical pool

- Discovered: 165751
- Ever alive: 32297
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
