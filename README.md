# SyndProxy private pool

## Current pool

- Alive now: 988
- Gold now: 522
- HTTP: 339 alive / 155 gold
- HTTPS: 241 alive / 89 gold
- SOCKS4: 202 alive / 136 gold
- SOCKS5: 206 alive / 142 gold

## Historical pool

- Discovered: 127357
- Ever alive: 19892
- Ever gold: 803

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
