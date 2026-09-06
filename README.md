# SyndProxy validated proxy pool

## Current pool

- Alive now: 414
- Gold now: 316
- HTTP: 75 alive / 53 gold
- HTTPS: 45 alive / 11 gold
- SOCKS4: 147 alive / 132 gold
- SOCKS5: 147 alive / 120 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48337
- Ever gold: 1529

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
