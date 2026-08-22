# SyndProxy private pool

## Current pool

- Alive now: 972
- Gold now: 402
- HTTP: 306 alive / 86 gold
- HTTPS: 211 alive / 25 gold
- SOCKS4: 211 alive / 134 gold
- SOCKS5: 244 alive / 157 gold

## Historical pool

- Discovered: 166609
- Ever alive: 32418
- Ever gold: 1180

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
