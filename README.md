# SyndProxy private pool

## Current pool

- Alive now: 1000
- Gold now: 398
- HTTP: 335 alive / 84 gold
- HTTPS: 204 alive / 24 gold
- SOCKS4: 212 alive / 134 gold
- SOCKS5: 249 alive / 156 gold

## Historical pool

- Discovered: 166608
- Ever alive: 32417
- Ever gold: 1180

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
