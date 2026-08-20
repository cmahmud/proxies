# SyndProxy private pool

## Current pool

- Alive now: 1565
- Gold now: 632
- HTTP: 593 alive / 236 gold
- HTTPS: 480 alive / 111 gold
- SOCKS4: 222 alive / 142 gold
- SOCKS5: 270 alive / 143 gold

## Historical pool

- Discovered: 142746
- Ever alive: 24616
- Ever gold: 1029

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
