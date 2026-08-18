# SyndProxy private pool

## Current pool

- Alive now: 997
- Gold now: 345
- HTTP: 322 alive / 55 gold
- HTTPS: 216 alive / 15 gold
- SOCKS4: 231 alive / 140 gold
- SOCKS5: 228 alive / 135 gold

## Historical pool

- Discovered: 107143
- Ever alive: 15094
- Ever gold: 479

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
