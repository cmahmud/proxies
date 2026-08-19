# SyndProxy private pool

## Current pool

- Alive now: 1060
- Gold now: 464
- HTTP: 388 alive / 132 gold
- HTTPS: 251 alive / 82 gold
- SOCKS4: 212 alive / 140 gold
- SOCKS5: 209 alive / 110 gold

## Historical pool

- Discovered: 117128
- Ever alive: 17455
- Ever gold: 664

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
