# SyndProxy private pool

## Current pool

- Alive now: 1045
- Gold now: 279
- HTTP: 406 alive / 28 gold
- HTTPS: 175 alive / 4 gold
- SOCKS4: 239 alive / 134 gold
- SOCKS5: 225 alive / 113 gold

## Historical pool

- Discovered: 100094
- Ever alive: 12654
- Ever gold: 398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
