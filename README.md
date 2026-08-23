# SyndProxy validated proxy pool

## Current pool

- Alive now: 459
- Gold now: 368
- HTTP: 84 alive / 51 gold
- HTTPS: 40 alive / 10 gold
- SOCKS4: 165 alive / 153 gold
- SOCKS5: 170 alive / 154 gold

## Historical pool

- Discovered: 174122
- Ever alive: 33048
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
