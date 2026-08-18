# SyndProxy private pool

## Current pool

- Alive now: 636
- Gold now: 233
- HTTP: 195 alive / 30 gold
- HTTPS: 90 alive / 5 gold
- SOCKS4: 163 alive / 104 gold
- SOCKS5: 188 alive / 94 gold

## Historical pool

- Discovered: 95381
- Ever alive: 10267
- Ever gold: 377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
