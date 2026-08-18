# SyndProxy private pool

## Current pool

- Alive now: 722
- Gold now: 205
- HTTP: 206 alive / 25 gold
- HTTPS: 101 alive / 7 gold
- SOCKS4: 205 alive / 100 gold
- SOCKS5: 210 alive / 73 gold

## Historical pool

- Discovered: 91695
- Ever alive: 8346
- Ever gold: 349

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
