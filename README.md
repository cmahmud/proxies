# SyndProxy private pool

## Current pool

- Alive now: 904
- Gold now: 407
- HTTP: 282 alive / 91 gold
- HTTPS: 189 alive / 26 gold
- SOCKS4: 212 alive / 135 gold
- SOCKS5: 221 alive / 155 gold

## Historical pool

- Discovered: 151679
- Ever alive: 27606
- Ever gold: 1100

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
