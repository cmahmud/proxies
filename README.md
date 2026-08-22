# SyndProxy private pool

## Current pool

- Alive now: 971
- Gold now: 382
- HTTP: 278 alive / 85 gold
- HTTPS: 237 alive / 28 gold
- SOCKS4: 205 alive / 121 gold
- SOCKS5: 251 alive / 148 gold

## Historical pool

- Discovered: 164184
- Ever alive: 32058
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
