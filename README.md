# SyndProxy private pool

## Current pool

- Alive now: 1205
- Gold now: 399
- HTTP: 431 alive / 103 gold
- HTTPS: 275 alive / 22 gold
- SOCKS4: 205 alive / 129 gold
- SOCKS5: 294 alive / 145 gold

## Historical pool

- Discovered: 136236
- Ever alive: 22566
- Ever gold: 908

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
