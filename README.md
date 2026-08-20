# SyndProxy private pool

## Current pool

- Alive now: 1554
- Gold now: 656
- HTTP: 588 alive / 250 gold
- HTTPS: 430 alive / 120 gold
- SOCKS4: 215 alive / 126 gold
- SOCKS5: 321 alive / 160 gold

## Historical pool

- Discovered: 143489
- Ever alive: 24807
- Ever gold: 1047

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
