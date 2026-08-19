# SyndProxy private pool

## Current pool

- Alive now: 1080
- Gold now: 548
- HTTP: 405 alive / 177 gold
- HTTPS: 268 alive / 115 gold
- SOCKS4: 207 alive / 120 gold
- SOCKS5: 200 alive / 136 gold

## Historical pool

- Discovered: 124841
- Ever alive: 19304
- Ever gold: 772

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
