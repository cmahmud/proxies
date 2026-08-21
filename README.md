# SyndProxy private pool

## Current pool

- Alive now: 799
- Gold now: 409
- HTTP: 203 alive / 82 gold
- HTTPS: 137 alive / 24 gold
- SOCKS4: 200 alive / 145 gold
- SOCKS5: 259 alive / 158 gold

## Historical pool

- Discovered: 155799
- Ever alive: 29346
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
