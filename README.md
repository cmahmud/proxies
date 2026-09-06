# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 386
- HTTP: 140 alive / 84 gold
- HTTPS: 54 alive / 24 gold
- SOCKS4: 155 alive / 128 gold
- SOCKS5: 180 alive / 150 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48008
- Ever gold: 1509

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
