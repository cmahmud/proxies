# SyndProxy private pool

## Current pool

- Alive now: 888
- Gold now: 266
- HTTP: 258 alive / 33 gold
- HTTPS: 176 alive / 5 gold
- SOCKS4: 209 alive / 123 gold
- SOCKS5: 245 alive / 105 gold

## Historical pool

- Discovered: 96705
- Ever alive: 11095
- Ever gold: 382

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
