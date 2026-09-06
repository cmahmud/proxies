# SyndProxy validated proxy pool

## Current pool

- Alive now: 420
- Gold now: 309
- HTTP: 84 alive / 50 gold
- HTTPS: 46 alive / 9 gold
- SOCKS4: 144 alive / 131 gold
- SOCKS5: 146 alive / 119 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48337
- Ever gold: 1529

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
