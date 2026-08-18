# SyndProxy private pool

## Current pool

- Alive now: 641
- Gold now: 234
- HTTP: 172 alive / 28 gold
- HTTPS: 95 alive / 8 gold
- SOCKS4: 184 alive / 112 gold
- SOCKS5: 190 alive / 86 gold

## Historical pool

- Discovered: 86746
- Ever alive: 6891
- Ever gold: 335

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
