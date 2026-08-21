# SyndProxy private pool

## Current pool

- Alive now: 1191
- Gold now: 427
- HTTP: 404 alive / 99 gold
- HTTPS: 285 alive / 24 gold
- SOCKS4: 236 alive / 146 gold
- SOCKS5: 266 alive / 158 gold

## Historical pool

- Discovered: 152746
- Ever alive: 28128
- Ever gold: 1104

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
