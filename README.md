# SyndProxy private pool

## Current pool

- Alive now: 1158
- Gold now: 549
- HTTP: 457 alive / 191 gold
- HTTPS: 300 alive / 115 gold
- SOCKS4: 206 alive / 113 gold
- SOCKS5: 195 alive / 130 gold

## Historical pool

- Discovered: 124850
- Ever alive: 19399
- Ever gold: 772

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
