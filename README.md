# SyndProxy private pool

## Current pool

- Alive now: 974
- Gold now: 298
- HTTP: 281 alive / 23 gold
- HTTPS: 199 alive / 4 gold
- SOCKS4: 251 alive / 148 gold
- SOCKS5: 243 alive / 123 gold

## Historical pool

- Discovered: 102809
- Ever alive: 12766
- Ever gold: 404

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
