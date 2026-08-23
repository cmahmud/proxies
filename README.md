# SyndProxy validated proxy pool

## Current pool

- Alive now: 381
- Gold now: 207
- HTTP: 116 alive / 47 gold
- HTTPS: 70 alive / 8 gold
- SOCKS4: 75 alive / 65 gold
- SOCKS5: 120 alive / 87 gold

## Historical pool

- Discovered: 169346
- Ever alive: 32700
- Ever gold: 1206

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
