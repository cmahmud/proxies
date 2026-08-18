# SyndProxy private pool

## Current pool

- Alive now: 669
- Gold now: 253
- HTTP: 177 alive / 32 gold
- HTTPS: 97 alive / 8 gold
- SOCKS4: 190 alive / 112 gold
- SOCKS5: 205 alive / 101 gold

## Historical pool

- Discovered: 95381
- Ever alive: 10238
- Ever gold: 377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
