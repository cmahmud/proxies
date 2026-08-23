# SyndProxy validated proxy pool

## Current pool

- Alive now: 544
- Gold now: 220
- HTTP: 212 alive / 56 gold
- HTTPS: 103 alive / 11 gold
- SOCKS4: 90 alive / 70 gold
- SOCKS5: 139 alive / 83 gold

## Historical pool

- Discovered: 169346
- Ever alive: 32684
- Ever gold: 1204

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
