# SyndProxy private pool

## Current pool

- Alive now: 1073
- Gold now: 525
- HTTP: 370 alive / 162 gold
- HTTPS: 273 alive / 91 gold
- SOCKS4: 210 alive / 123 gold
- SOCKS5: 220 alive / 149 gold

## Historical pool

- Discovered: 124834
- Ever alive: 19192
- Ever gold: 731

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
