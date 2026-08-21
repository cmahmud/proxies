# SyndProxy private pool

## Current pool

- Alive now: 991
- Gold now: 419
- HTTP: 337 alive / 105 gold
- HTTPS: 199 alive / 32 gold
- SOCKS4: 218 alive / 137 gold
- SOCKS5: 237 alive / 145 gold

## Historical pool

- Discovered: 160259
- Ever alive: 30718
- Ever gold: 1147

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
