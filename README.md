# SyndProxy private pool

## Current pool

- Alive now: 1488
- Gold now: 607
- HTTP: 567 alive / 213 gold
- HTTPS: 462 alive / 106 gold
- SOCKS4: 238 alive / 150 gold
- SOCKS5: 221 alive / 138 gold

## Historical pool

- Discovered: 140469
- Ever alive: 23745
- Ever gold: 956

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
