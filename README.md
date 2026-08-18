# SyndProxy private pool

## Current pool

- Alive now: 748
- Gold now: 261
- HTTP: 225 alive / 29 gold
- HTTPS: 120 alive / 4 gold
- SOCKS4: 197 alive / 118 gold
- SOCKS5: 206 alive / 110 gold

## Historical pool

- Discovered: 99142
- Ever alive: 11915
- Ever gold: 389

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
