# SyndProxy private pool

## Current pool

- Alive now: 1151
- Gold now: 391
- HTTP: 381 alive / 103 gold
- HTTPS: 266 alive / 22 gold
- SOCKS4: 205 alive / 121 gold
- SOCKS5: 299 alive / 145 gold

## Historical pool

- Discovered: 136236
- Ever alive: 22631
- Ever gold: 908

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
