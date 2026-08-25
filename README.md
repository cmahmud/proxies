# SyndProxy validated proxy pool

## Current pool

- Alive now: 566
- Gold now: 419
- HTTP: 101 alive / 63 gold
- HTTPS: 85 alive / 20 gold
- SOCKS4: 179 alive / 160 gold
- SOCKS5: 201 alive / 176 gold

## Historical pool

- Discovered: 183892
- Ever alive: 35986
- Ever gold: 1261

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
