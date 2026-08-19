# SyndProxy private pool

## Current pool

- Alive now: 1081
- Gold now: 483
- HTTP: 378 alive / 127 gold
- HTTPS: 269 alive / 79 gold
- SOCKS4: 213 alive / 124 gold
- SOCKS5: 221 alive / 153 gold

## Historical pool

- Discovered: 119696
- Ever alive: 17893
- Ever gold: 693

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
