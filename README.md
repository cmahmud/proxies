# SyndProxy private pool

## Current pool

- Alive now: 775
- Gold now: 386
- HTTP: 201 alive / 78 gold
- HTTPS: 145 alive / 16 gold
- SOCKS4: 213 alive / 147 gold
- SOCKS5: 216 alive / 145 gold

## Historical pool

- Discovered: 148343
- Ever alive: 26406
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
