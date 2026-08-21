# SyndProxy private pool

## Current pool

- Alive now: 1124
- Gold now: 438
- HTTP: 398 alive / 107 gold
- HTTPS: 250 alive / 31 gold
- SOCKS4: 210 alive / 141 gold
- SOCKS5: 266 alive / 159 gold

## Historical pool

- Discovered: 153726
- Ever alive: 28656
- Ever gold: 1110

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
