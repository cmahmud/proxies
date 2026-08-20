# SyndProxy private pool

## Current pool

- Alive now: 725
- Gold now: 360
- HTTP: 187 alive / 83 gold
- HTTPS: 140 alive / 18 gold
- SOCKS4: 194 alive / 133 gold
- SOCKS5: 204 alive / 126 gold

## Historical pool

- Discovered: 149496
- Ever alive: 26593
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
