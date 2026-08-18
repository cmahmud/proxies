# SyndProxy private pool

## Current pool

- Alive now: 945
- Gold now: 348
- HTTP: 299 alive / 52 gold
- HTTPS: 188 alive / 13 gold
- SOCKS4: 220 alive / 133 gold
- SOCKS5: 238 alive / 150 gold

## Historical pool

- Discovered: 107131
- Ever alive: 14909
- Ever gold: 478

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
