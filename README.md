# SyndProxy private pool

## Current pool

- Alive now: 1081
- Gold now: 434
- HTTP: 343 alive / 104 gold
- HTTPS: 249 alive / 24 gold
- SOCKS4: 221 alive / 146 gold
- SOCKS5: 268 alive / 160 gold

## Historical pool

- Discovered: 152746
- Ever alive: 28120
- Ever gold: 1104

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
