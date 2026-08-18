# SyndProxy private pool

## Current pool

- Alive now: 677
- Gold now: 253
- HTTP: 173 alive / 31 gold
- HTTPS: 98 alive / 8 gold
- SOCKS4: 191 alive / 111 gold
- SOCKS5: 215 alive / 103 gold

## Historical pool

- Discovered: 95381
- Ever alive: 10237
- Ever gold: 377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
