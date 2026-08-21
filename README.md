# SyndProxy private pool

## Current pool

- Alive now: 1133
- Gold now: 390
- HTTP: 373 alive / 86 gold
- HTTPS: 263 alive / 19 gold
- SOCKS4: 236 alive / 147 gold
- SOCKS5: 261 alive / 138 gold

## Historical pool

- Discovered: 158238
- Ever alive: 30004
- Ever gold: 1139

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
