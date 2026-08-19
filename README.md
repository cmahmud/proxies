# SyndProxy private pool

## Current pool

- Alive now: 1331
- Gold now: 544
- HTTP: 515 alive / 188 gold
- HTTPS: 342 alive / 53 gold
- SOCKS4: 233 alive / 146 gold
- SOCKS5: 241 alive / 157 gold

## Historical pool

- Discovered: 125596
- Ever alive: 19575
- Ever gold: 774

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
