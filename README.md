# SyndProxy private pool

## Current pool

- Alive now: 646
- Gold now: 256
- HTTP: 147 alive / 30 gold
- HTTPS: 86 alive / 6 gold
- SOCKS4: 218 alive / 132 gold
- SOCKS5: 195 alive / 88 gold

## Historical pool

- Discovered: 91741
- Ever alive: 9108
- Ever gold: 363

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
