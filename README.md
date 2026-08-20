# SyndProxy private pool

## Current pool

- Alive now: 682
- Gold now: 382
- HTTP: 177 alive / 72 gold
- HTTPS: 106 alive / 16 gold
- SOCKS4: 198 alive / 153 gold
- SOCKS5: 201 alive / 141 gold

## Historical pool

- Discovered: 146659
- Ever alive: 25702
- Ever gold: 1071

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
