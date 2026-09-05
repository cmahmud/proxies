# SyndProxy validated proxy pool

## Current pool

- Alive now: 394
- Gold now: 306
- HTTP: 103 alive / 75 gold
- HTTPS: 38 alive / 15 gold
- SOCKS4: 81 alive / 72 gold
- SOCKS5: 172 alive / 144 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47835
- Ever gold: 1498

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
