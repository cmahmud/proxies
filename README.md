# SyndProxy private pool

## Current pool

- Alive now: 1222
- Gold now: 414
- HTTP: 434 alive / 105 gold
- HTTPS: 324 alive / 30 gold
- SOCKS4: 231 alive / 152 gold
- SOCKS5: 233 alive / 127 gold

## Historical pool

- Discovered: 159261
- Ever alive: 30328
- Ever gold: 1144

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
