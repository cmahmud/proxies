# SyndProxy validated proxy pool

## Current pool

- Alive now: 422
- Gold now: 316
- HTTP: 106 alive / 80 gold
- HTTPS: 63 alive / 20 gold
- SOCKS4: 89 alive / 78 gold
- SOCKS5: 164 alive / 138 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47942
- Ever gold: 1505

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
