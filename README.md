# SyndProxy private pool

## Current pool

- Alive now: 1020
- Gold now: 359
- HTTP: 326 alive / 70 gold
- HTTPS: 234 alive / 13 gold
- SOCKS4: 210 alive / 130 gold
- SOCKS5: 250 alive / 146 gold

## Historical pool

- Discovered: 129290
- Ever alive: 20361
- Ever gold: 865

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
