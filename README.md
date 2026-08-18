# SyndProxy private pool

## Current pool

- Alive now: 1003
- Gold now: 343
- HTTP: 335 alive / 49 gold
- HTTPS: 205 alive / 11 gold
- SOCKS4: 237 alive / 144 gold
- SOCKS5: 226 alive / 139 gold

## Historical pool

- Discovered: 107067
- Ever alive: 14660
- Ever gold: 468

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
