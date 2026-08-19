# SyndProxy private pool

## Current pool

- Alive now: 1043
- Gold now: 472
- HTTP: 368 alive / 133 gold
- HTTPS: 247 alive / 90 gold
- SOCKS4: 217 alive / 140 gold
- SOCKS5: 211 alive / 109 gold

## Historical pool

- Discovered: 117124
- Ever alive: 17451
- Ever gold: 663

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
