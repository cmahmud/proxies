# SyndProxy private pool

## Current pool

- Alive now: 1021
- Gold now: 526
- HTTP: 349 alive / 161 gold
- HTTPS: 271 alive / 89 gold
- SOCKS4: 199 alive / 141 gold
- SOCKS5: 202 alive / 135 gold

## Historical pool

- Discovered: 119849
- Ever alive: 18428
- Ever gold: 718

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
