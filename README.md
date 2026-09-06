# SyndProxy validated proxy pool

## Current pool

- Alive now: 474
- Gold now: 383
- HTTP: 97 alive / 68 gold
- HTTPS: 37 alive / 11 gold
- SOCKS4: 168 alive / 154 gold
- SOCKS5: 172 alive / 150 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48183
- Ever gold: 1522

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
