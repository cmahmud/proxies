# SyndProxy private pool

## Current pool

- Alive now: 1568
- Gold now: 656
- HTTP: 592 alive / 251 gold
- HTTPS: 497 alive / 120 gold
- SOCKS4: 206 alive / 127 gold
- SOCKS5: 273 alive / 158 gold

## Historical pool

- Discovered: 143487
- Ever alive: 24794
- Ever gold: 1046

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
