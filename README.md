# SyndProxy validated proxy pool

## Current pool

- Alive now: 544
- Gold now: 381
- HTTP: 150 alive / 81 gold
- HTTPS: 56 alive / 23 gold
- SOCKS4: 155 alive / 128 gold
- SOCKS5: 183 alive / 149 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48010
- Ever gold: 1509

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
