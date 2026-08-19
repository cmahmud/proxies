# SyndProxy private pool

## Current pool

- Alive now: 1054
- Gold now: 346
- HTTP: 390 alive / 67 gold
- HTTPS: 202 alive / 12 gold
- SOCKS4: 241 alive / 140 gold
- SOCKS5: 221 alive / 127 gold

## Historical pool

- Discovered: 129268
- Ever alive: 20246
- Ever gold: 864

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
