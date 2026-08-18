# SyndProxy private pool

## Current pool

- Alive now: 915
- Gold now: 266
- HTTP: 263 alive / 33 gold
- HTTPS: 192 alive / 5 gold
- SOCKS4: 212 alive / 122 gold
- SOCKS5: 248 alive / 106 gold

## Historical pool

- Discovered: 96705
- Ever alive: 11094
- Ever gold: 382

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
