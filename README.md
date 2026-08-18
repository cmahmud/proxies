# SyndProxy private pool

## Current pool

- Alive now: 697
- Gold now: 262
- HTTP: 190 alive / 33 gold
- HTTPS: 100 alive / 3 gold
- SOCKS4: 221 alive / 132 gold
- SOCKS5: 186 alive / 94 gold

## Historical pool

- Discovered: 95396
- Ever alive: 10668
- Ever gold: 382

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
