# SyndProxy validated proxy pool

## Current pool

- Alive now: 395
- Gold now: 307
- HTTP: 102 alive / 74 gold
- HTTPS: 37 alive / 17 gold
- SOCKS4: 85 alive / 72 gold
- SOCKS5: 171 alive / 144 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47831
- Ever gold: 1497

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
