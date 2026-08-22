# SyndProxy private pool

## Current pool

- Alive now: 1069
- Gold now: 423
- HTTP: 335 alive / 86 gold
- HTTPS: 222 alive / 26 gold
- SOCKS4: 234 alive / 141 gold
- SOCKS5: 278 alive / 170 gold

## Historical pool

- Discovered: 164944
- Ever alive: 32214
- Ever gold: 1174

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
