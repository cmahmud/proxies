# SyndProxy private pool

## Current pool

- Alive now: 709
- Gold now: 363
- HTTP: 147 alive / 66 gold
- HTTPS: 150 alive / 15 gold
- SOCKS4: 215 alive / 146 gold
- SOCKS5: 197 alive / 136 gold

## Historical pool

- Discovered: 148336
- Ever alive: 26268
- Ever gold: 1080

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
