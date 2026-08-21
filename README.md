# SyndProxy private pool

## Current pool

- Alive now: 1453
- Gold now: 444
- HTTP: 533 alive / 106 gold
- HTTPS: 414 alive / 30 gold
- SOCKS4: 244 alive / 149 gold
- SOCKS5: 262 alive / 159 gold

## Historical pool

- Discovered: 160009
- Ever alive: 30501
- Ever gold: 1145

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
