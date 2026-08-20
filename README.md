# SyndProxy private pool

## Current pool

- Alive now: 1902
- Gold now: 698
- HTTP: 748 alive / 236 gold
- HTTPS: 617 alive / 148 gold
- SOCKS4: 221 alive / 148 gold
- SOCKS5: 316 alive / 166 gold

## Historical pool

- Discovered: 142715
- Ever alive: 24471
- Ever gold: 1026

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
