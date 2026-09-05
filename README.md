# SyndProxy validated proxy pool

## Current pool

- Alive now: 394
- Gold now: 311
- HTTP: 102 alive / 74 gold
- HTTPS: 36 alive / 17 gold
- SOCKS4: 84 alive / 73 gold
- SOCKS5: 172 alive / 147 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47831
- Ever gold: 1497

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
