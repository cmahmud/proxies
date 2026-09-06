# SyndProxy validated proxy pool

## Current pool

- Alive now: 388
- Gold now: 316
- HTTP: 73 alive / 49 gold
- HTTPS: 28 alive / 11 gold
- SOCKS4: 143 alive / 135 gold
- SOCKS5: 144 alive / 121 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48322
- Ever gold: 1529

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
