# SyndProxy private pool

## Current pool

- Alive now: 851
- Gold now: 383
- HTTP: 252 alive / 73 gold
- HTTPS: 179 alive / 14 gold
- SOCKS4: 209 alive / 148 gold
- SOCKS5: 211 alive / 148 gold

## Historical pool

- Discovered: 148776
- Ever alive: 26473
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
