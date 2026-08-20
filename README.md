# SyndProxy private pool

## Current pool

- Alive now: 744
- Gold now: 375
- HTTP: 209 alive / 69 gold
- HTTPS: 105 alive / 22 gold
- SOCKS4: 225 alive / 143 gold
- SOCKS5: 205 alive / 141 gold

## Historical pool

- Discovered: 145552
- Ever alive: 25424
- Ever gold: 1059

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
