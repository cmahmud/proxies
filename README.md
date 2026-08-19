# SyndProxy private pool

## Current pool

- Alive now: 1225
- Gold now: 391
- HTTP: 428 alive / 89 gold
- HTTPS: 327 alive / 14 gold
- SOCKS4: 220 alive / 128 gold
- SOCKS5: 250 alive / 160 gold

## Historical pool

- Discovered: 131851
- Ever alive: 21268
- Ever gold: 880

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
