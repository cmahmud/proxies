# SyndProxy private pool

## Current pool

- Alive now: 814
- Gold now: 413
- HTTP: 213 alive / 77 gold
- HTTPS: 153 alive / 24 gold
- SOCKS4: 222 alive / 152 gold
- SOCKS5: 226 alive / 160 gold

## Historical pool

- Discovered: 151067
- Ever alive: 27387
- Ever gold: 1096

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
