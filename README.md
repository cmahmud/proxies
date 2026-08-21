# SyndProxy private pool

## Current pool

- Alive now: 786
- Gold now: 407
- HTTP: 218 alive / 87 gold
- HTTPS: 103 alive / 17 gold
- SOCKS4: 224 alive / 150 gold
- SOCKS5: 241 alive / 153 gold

## Historical pool

- Discovered: 155739
- Ever alive: 29285
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
