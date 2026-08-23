# SyndProxy validated proxy pool

## Current pool

- Alive now: 495
- Gold now: 218
- HTTP: 146 alive / 54 gold
- HTTPS: 120 alive / 11 gold
- SOCKS4: 87 alive / 70 gold
- SOCKS5: 142 alive / 83 gold

## Historical pool

- Discovered: 169346
- Ever alive: 32684
- Ever gold: 1204

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
