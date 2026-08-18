# SyndProxy private pool

## Current pool

- Alive now: 983
- Gold now: 342
- HTTP: 317 alive / 48 gold
- HTTPS: 199 alive / 11 gold
- SOCKS4: 235 alive / 144 gold
- SOCKS5: 232 alive / 139 gold

## Historical pool

- Discovered: 107067
- Ever alive: 14663
- Ever gold: 468

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
