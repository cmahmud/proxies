# SyndProxy private pool

## Current pool

- Alive now: 1158
- Gold now: 396
- HTTP: 413 alive / 92 gold
- HTTPS: 280 alive / 15 gold
- SOCKS4: 215 alive / 128 gold
- SOCKS5: 250 alive / 161 gold

## Historical pool

- Discovered: 131850
- Ever alive: 21249
- Ever gold: 880

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
