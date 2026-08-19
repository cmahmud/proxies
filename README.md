# SyndProxy private pool

## Current pool

- Alive now: 990
- Gold now: 514
- HTTP: 344 alive / 151 gold
- HTTPS: 237 alive / 87 gold
- SOCKS4: 202 alive / 134 gold
- SOCKS5: 207 alive / 142 gold

## Historical pool

- Discovered: 127357
- Ever alive: 19892
- Ever gold: 803

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
