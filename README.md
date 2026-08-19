# SyndProxy private pool

## Current pool

- Alive now: 1123
- Gold now: 544
- HTTP: 449 alive / 163 gold
- HTTPS: 260 alive / 94 gold
- SOCKS4: 203 alive / 145 gold
- SOCKS5: 211 alive / 142 gold

## Historical pool

- Discovered: 123170
- Ever alive: 18855
- Ever gold: 729

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
