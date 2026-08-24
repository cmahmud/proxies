# SyndProxy validated proxy pool

## Current pool

- Alive now: 511
- Gold now: 388
- HTTP: 97 alive / 54 gold
- HTTPS: 59 alive / 14 gold
- SOCKS4: 169 alive / 157 gold
- SOCKS5: 186 alive / 163 gold

## Historical pool

- Discovered: 179924
- Ever alive: 33532
- Ever gold: 1240

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
