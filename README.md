# SyndProxy private pool

## Current pool

- Alive now: 1036
- Gold now: 425
- HTTP: 328 alive / 93 gold
- HTTPS: 242 alive / 23 gold
- SOCKS4: 215 alive / 151 gold
- SOCKS5: 251 alive / 158 gold

## Historical pool

- Discovered: 158911
- Ever alive: 30111
- Ever gold: 1140

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
