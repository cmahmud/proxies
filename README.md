# SyndProxy private pool

## Current pool

- Alive now: 761
- Gold now: 396
- HTTP: 190 alive / 86 gold
- HTTPS: 111 alive / 22 gold
- SOCKS4: 218 alive / 148 gold
- SOCKS5: 242 alive / 140 gold

## Historical pool

- Discovered: 155693
- Ever alive: 29225
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
