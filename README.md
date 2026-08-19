# SyndProxy private pool

## Current pool

- Alive now: 1079
- Gold now: 543
- HTTP: 394 alive / 178 gold
- HTTPS: 276 alive / 115 gold
- SOCKS4: 212 alive / 116 gold
- SOCKS5: 197 alive / 134 gold

## Historical pool

- Discovered: 124841
- Ever alive: 19304
- Ever gold: 772

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
