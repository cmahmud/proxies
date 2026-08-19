# SyndProxy private pool

## Current pool

- Alive now: 937
- Gold now: 473
- HTTP: 295 alive / 126 gold
- HTTPS: 243 alive / 86 gold
- SOCKS4: 212 alive / 143 gold
- SOCKS5: 187 alive / 118 gold

## Historical pool

- Discovered: 117130
- Ever alive: 17476
- Ever gold: 664

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
