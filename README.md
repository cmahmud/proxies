# SyndProxy private pool

## Current pool

- Alive now: 760
- Gold now: 406
- HTTP: 212 alive / 85 gold
- HTTPS: 115 alive / 20 gold
- SOCKS4: 216 alive / 149 gold
- SOCKS5: 217 alive / 152 gold

## Historical pool

- Discovered: 155785
- Ever alive: 29297
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
