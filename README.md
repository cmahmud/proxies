# SyndProxy private pool

## Current pool

- Alive now: 663
- Gold now: 258
- HTTP: 168 alive / 32 gold
- HTTPS: 89 alive / 7 gold
- SOCKS4: 209 alive / 132 gold
- SOCKS5: 197 alive / 87 gold

## Historical pool

- Discovered: 91741
- Ever alive: 9108
- Ever gold: 363

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
