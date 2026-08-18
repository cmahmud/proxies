# SyndProxy private pool

## Current pool

- Alive now: 915
- Gold now: 210
- HTTP: 347 alive / 26 gold
- HTTPS: 143 alive / 9 gold
- SOCKS4: 201 alive / 96 gold
- SOCKS5: 224 alive / 79 gold

## Historical pool

- Discovered: 86776
- Ever alive: 7932
- Ever gold: 343

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
