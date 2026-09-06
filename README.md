# SyndProxy validated proxy pool

## Current pool

- Alive now: 406
- Gold now: 316
- HTTP: 78 alive / 56 gold
- HTTPS: 37 alive / 7 gold
- SOCKS4: 147 alive / 133 gold
- SOCKS5: 144 alive / 120 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48354
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
