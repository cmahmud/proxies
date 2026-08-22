# SyndProxy private pool

## Current pool

- Alive now: 982
- Gold now: 341
- HTTP: 337 alive / 83 gold
- HTTPS: 254 alive / 25 gold
- SOCKS4: 196 alive / 140 gold
- SOCKS5: 195 alive / 93 gold

## Historical pool

- Discovered: 167096
- Ever alive: 32499
- Ever gold: 1184

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
