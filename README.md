# SyndProxy validated proxy pool

## Current pool

- Alive now: 458
- Gold now: 316
- HTTP: 176 alive / 80 gold
- HTTPS: 30 alive / 18 gold
- SOCKS4: 81 alive / 71 gold
- SOCKS5: 171 alive / 147 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47823
- Ever gold: 1495

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
