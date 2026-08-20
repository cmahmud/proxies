# SyndProxy private pool

## Current pool

- Alive now: 679
- Gold now: 394
- HTTP: 155 alive / 71 gold
- HTTPS: 109 alive / 20 gold
- SOCKS4: 200 alive / 144 gold
- SOCKS5: 215 alive / 159 gold

## Historical pool

- Discovered: 145572
- Ever alive: 25523
- Ever gold: 1063

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
