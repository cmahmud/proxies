# SyndProxy private pool

## Current pool

- Alive now: 976
- Gold now: 388
- HTTP: 302 alive / 81 gold
- HTTPS: 218 alive / 25 gold
- SOCKS4: 197 alive / 123 gold
- SOCKS5: 259 alive / 159 gold

## Historical pool

- Discovered: 164917
- Ever alive: 32144
- Ever gold: 1171

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
