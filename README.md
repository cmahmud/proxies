# SyndProxy private pool

## Current pool

- Alive now: 750
- Gold now: 388
- HTTP: 209 alive / 86 gold
- HTTPS: 111 alive / 24 gold
- SOCKS4: 192 alive / 121 gold
- SOCKS5: 238 alive / 157 gold

## Historical pool

- Discovered: 156417
- Ever alive: 29466
- Ever gold: 1127

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
