# SyndProxy private pool

## Current pool

- Alive now: 1052
- Gold now: 525
- HTTP: 387 alive / 158 gold
- HTTPS: 254 alive / 88 gold
- SOCKS4: 203 alive / 137 gold
- SOCKS5: 208 alive / 142 gold

## Historical pool

- Discovered: 127357
- Ever alive: 19892
- Ever gold: 803

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
