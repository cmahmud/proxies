# SyndProxy validated proxy pool

## Current pool

- Alive now: 537
- Gold now: 220
- HTTP: 200 alive / 56 gold
- HTTPS: 107 alive / 11 gold
- SOCKS4: 90 alive / 70 gold
- SOCKS5: 140 alive / 83 gold

## Historical pool

- Discovered: 169346
- Ever alive: 32684
- Ever gold: 1204

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
