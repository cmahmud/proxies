# SyndProxy validated proxy pool

## Current pool

- Alive now: 518
- Gold now: 335
- HTTP: 112 alive / 39 gold
- HTTPS: 66 alive / 9 gold
- SOCKS4: 165 alive / 148 gold
- SOCKS5: 175 alive / 139 gold

## Historical pool

- Discovered: 170572
- Ever alive: 32792
- Ever gold: 1212

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
