# SyndProxy private pool

## Current pool

- Alive now: 1031
- Gold now: 426
- HTTP: 308 alive / 90 gold
- HTTPS: 201 alive / 23 gold
- SOCKS4: 228 alive / 141 gold
- SOCKS5: 294 alive / 172 gold

## Historical pool

- Discovered: 164947
- Ever alive: 32216
- Ever gold: 1174

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
