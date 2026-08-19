# SyndProxy private pool

## Current pool

- Alive now: 914
- Gold now: 299
- HTTP: 325 alive / 64 gold
- HTTPS: 222 alive / 18 gold
- SOCKS4: 199 alive / 117 gold
- SOCKS5: 168 alive / 100 gold

## Historical pool

- Discovered: 109991
- Ever alive: 15650
- Ever gold: 499

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
