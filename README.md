# SyndProxy validated proxy pool

## Current pool

- Alive now: 481
- Gold now: 367
- HTTP: 96 alive / 52 gold
- HTTPS: 41 alive / 11 gold
- SOCKS4: 163 alive / 151 gold
- SOCKS5: 181 alive / 153 gold

## Historical pool

- Discovered: 174122
- Ever alive: 33055
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
