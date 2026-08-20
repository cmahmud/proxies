# SyndProxy private pool

## Current pool

- Alive now: 1738
- Gold now: 705
- HTTP: 657 alive / 235 gold
- HTTPS: 529 alive / 145 gold
- SOCKS4: 242 alive / 158 gold
- SOCKS5: 310 alive / 167 gold

## Historical pool

- Discovered: 142702
- Ever alive: 24368
- Ever gold: 1021

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
