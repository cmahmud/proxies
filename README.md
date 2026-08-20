# SyndProxy private pool

## Current pool

- Alive now: 1461
- Gold now: 564
- HTTP: 481 alive / 188 gold
- HTTPS: 407 alive / 90 gold
- SOCKS4: 240 alive / 151 gold
- SOCKS5: 333 alive / 135 gold

## Historical pool

- Discovered: 140462
- Ever alive: 23612
- Ever gold: 924

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
