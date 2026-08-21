# SyndProxy private pool

## Current pool

- Alive now: 1305
- Gold now: 446
- HTTP: 453 alive / 103 gold
- HTTPS: 323 alive / 30 gold
- SOCKS4: 245 alive / 152 gold
- SOCKS5: 284 alive / 161 gold

## Historical pool

- Discovered: 159282
- Ever alive: 30458
- Ever gold: 1145

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
