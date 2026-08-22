# SyndProxy private pool

## Current pool

- Alive now: 970
- Gold now: 438
- HTTP: 303 alive / 94 gold
- HTTPS: 229 alive / 31 gold
- SOCKS4: 192 alive / 140 gold
- SOCKS5: 246 alive / 173 gold

## Historical pool

- Discovered: 161986
- Ever alive: 31258
- Ever gold: 1156

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
