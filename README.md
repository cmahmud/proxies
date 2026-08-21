# SyndProxy private pool

## Current pool

- Alive now: 801
- Gold now: 408
- HTTP: 236 alive / 90 gold
- HTTPS: 104 alive / 18 gold
- SOCKS4: 220 alive / 149 gold
- SOCKS5: 241 alive / 151 gold

## Historical pool

- Discovered: 155739
- Ever alive: 29281
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
