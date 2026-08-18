# SyndProxy private pool

## Current pool

- Alive now: 609
- Gold now: 233
- HTTP: 170 alive / 30 gold
- HTTPS: 90 alive / 5 gold
- SOCKS4: 164 alive / 104 gold
- SOCKS5: 185 alive / 94 gold

## Historical pool

- Discovered: 95381
- Ever alive: 10241
- Ever gold: 377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
