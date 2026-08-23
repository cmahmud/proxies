# SyndProxy validated proxy pool

## Current pool

- Alive now: 469
- Gold now: 368
- HTTP: 93 alive / 53 gold
- HTTPS: 36 alive / 9 gold
- SOCKS4: 170 alive / 152 gold
- SOCKS5: 170 alive / 154 gold

## Historical pool

- Discovered: 174122
- Ever alive: 33051
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
