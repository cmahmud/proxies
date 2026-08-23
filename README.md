# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 335
- HTTP: 109 alive / 39 gold
- HTTPS: 64 alive / 9 gold
- SOCKS4: 168 alive / 148 gold
- SOCKS5: 174 alive / 139 gold

## Historical pool

- Discovered: 170572
- Ever alive: 32792
- Ever gold: 1212

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
