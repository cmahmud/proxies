# SyndProxy private pool

## Current pool

- Alive now: 988
- Gold now: 509
- HTTP: 364 alive / 183 gold
- HTTPS: 232 alive / 103 gold
- SOCKS4: 203 alive / 110 gold
- SOCKS5: 189 alive / 113 gold

## Historical pool

- Discovered: 124845
- Ever alive: 19374
- Ever gold: 772

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
