# SyndProxy private pool

## Current pool

- Alive now: 828
- Gold now: 382
- HTTP: 261 alive / 86 gold
- HTTPS: 157 alive / 30 gold
- SOCKS4: 204 alive / 135 gold
- SOCKS5: 206 alive / 131 gold

## Historical pool

- Discovered: 162762
- Ever alive: 31595
- Ever gold: 1162

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
