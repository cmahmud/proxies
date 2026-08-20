# SyndProxy private pool

## Current pool

- Alive now: 763
- Gold now: 363
- HTTP: 173 alive / 67 gold
- HTTPS: 164 alive / 15 gold
- SOCKS4: 227 alive / 146 gold
- SOCKS5: 199 alive / 135 gold

## Historical pool

- Discovered: 148336
- Ever alive: 26275
- Ever gold: 1080

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
