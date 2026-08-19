# SyndProxy private pool

## Current pool

- Alive now: 1058
- Gold now: 525
- HTTP: 387 alive / 159 gold
- HTTPS: 261 alive / 94 gold
- SOCKS4: 203 alive / 134 gold
- SOCKS5: 207 alive / 138 gold

## Historical pool

- Discovered: 127357
- Ever alive: 19894
- Ever gold: 803

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
