# SyndProxy private pool

## Current pool

- Alive now: 696
- Gold now: 398
- HTTP: 149 alive / 80 gold
- HTTPS: 118 alive / 20 gold
- SOCKS4: 220 alive / 151 gold
- SOCKS5: 209 alive / 147 gold

## Historical pool

- Discovered: 144750
- Ever alive: 25213
- Ever gold: 1057

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
