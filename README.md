# SyndProxy validated proxy pool

## Current pool

- Alive now: 420
- Gold now: 305
- HTTP: 76 alive / 45 gold
- HTTPS: 48 alive / 11 gold
- SOCKS4: 149 alive / 132 gold
- SOCKS5: 147 alive / 117 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48337
- Ever gold: 1529

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
