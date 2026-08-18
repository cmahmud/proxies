# SyndProxy private pool

## Current pool

- Alive now: 784
- Gold now: 264
- HTTP: 215 alive / 33 gold
- HTTPS: 157 alive / 4 gold
- SOCKS4: 212 alive / 131 gold
- SOCKS5: 200 alive / 96 gold

## Historical pool

- Discovered: 95396
- Ever alive: 10663
- Ever gold: 379

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
