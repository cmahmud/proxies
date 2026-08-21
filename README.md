# SyndProxy private pool

## Current pool

- Alive now: 848
- Gold now: 416
- HTTP: 220 alive / 82 gold
- HTTPS: 151 alive / 25 gold
- SOCKS4: 217 alive / 143 gold
- SOCKS5: 260 alive / 166 gold

## Historical pool

- Discovered: 155796
- Ever alive: 29338
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
