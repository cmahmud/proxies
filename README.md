# SyndProxy private pool

## Current pool

- Alive now: 747
- Gold now: 371
- HTTP: 233 alive / 70 gold
- HTTPS: 123 alive / 17 gold
- SOCKS4: 185 alive / 140 gold
- SOCKS5: 206 alive / 144 gold

## Historical pool

- Discovered: 147187
- Ever alive: 25827
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
