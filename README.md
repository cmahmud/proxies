# SyndProxy private pool

## Current pool

- Alive now: 777
- Gold now: 383
- HTTP: 197 alive / 77 gold
- HTTPS: 150 alive / 15 gold
- SOCKS4: 213 alive / 148 gold
- SOCKS5: 217 alive / 143 gold

## Historical pool

- Discovered: 148343
- Ever alive: 26406
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
