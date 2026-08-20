# SyndProxy private pool

## Current pool

- Alive now: 1737
- Gold now: 707
- HTTP: 660 alive / 237 gold
- HTTPS: 529 alive / 145 gold
- SOCKS4: 238 alive / 158 gold
- SOCKS5: 310 alive / 167 gold

## Historical pool

- Discovered: 142702
- Ever alive: 24368
- Ever gold: 1020

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
