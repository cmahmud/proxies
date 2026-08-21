# SyndProxy private pool

## Current pool

- Alive now: 989
- Gold now: 387
- HTTP: 308 alive / 87 gold
- HTTPS: 222 alive / 27 gold
- SOCKS4: 222 alive / 144 gold
- SOCKS5: 237 alive / 129 gold

## Historical pool

- Discovered: 160993
- Ever alive: 30907
- Ever gold: 1152

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
