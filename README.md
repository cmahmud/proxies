# SyndProxy validated proxy pool

## Current pool

- Alive now: 503
- Gold now: 379
- HTTP: 102 alive / 63 gold
- HTTPS: 42 alive / 13 gold
- SOCKS4: 178 alive / 150 gold
- SOCKS5: 181 alive / 153 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48115
- Ever gold: 1519

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
