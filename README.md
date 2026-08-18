# SyndProxy private pool

## Current pool

- Alive now: 1052
- Gold now: 229
- HTTP: 574 alive / 28 gold
- HTTPS: 105 alive / 8 gold
- SOCKS4: 183 alive / 109 gold
- SOCKS5: 190 alive / 84 gold

## Historical pool

- Discovered: 86746
- Ever alive: 7318
- Ever gold: 335

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
