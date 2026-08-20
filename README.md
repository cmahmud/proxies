# SyndProxy private pool

## Current pool

- Alive now: 967
- Gold now: 387
- HTTP: 299 alive / 79 gold
- HTTPS: 213 alive / 25 gold
- SOCKS4: 210 alive / 131 gold
- SOCKS5: 245 alive / 152 gold

## Historical pool

- Discovered: 144732
- Ever alive: 24937
- Ever gold: 1051

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
