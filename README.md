# SyndProxy private pool

## Current pool

- Alive now: 803
- Gold now: 261
- HTTP: 216 alive / 32 gold
- HTTPS: 166 alive / 4 gold
- SOCKS4: 214 alive / 129 gold
- SOCKS5: 207 alive / 96 gold

## Historical pool

- Discovered: 95396
- Ever alive: 10663
- Ever gold: 378

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
