# SyndProxy private pool

## Current pool

- Alive now: 1075
- Gold now: 541
- HTTP: 359 alive / 163 gold
- HTTPS: 265 alive / 96 gold
- SOCKS4: 240 alive / 145 gold
- SOCKS5: 211 alive / 137 gold

## Historical pool

- Discovered: 123170
- Ever alive: 18891
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
