# SyndProxy private pool

## Current pool

- Alive now: 675
- Gold now: 253
- HTTP: 178 alive / 32 gold
- HTTPS: 97 alive / 8 gold
- SOCKS4: 192 alive / 112 gold
- SOCKS5: 208 alive / 101 gold

## Historical pool

- Discovered: 95381
- Ever alive: 10238
- Ever gold: 377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
