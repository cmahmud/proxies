# SyndProxy private pool

## Current pool

- Alive now: 674
- Gold now: 355
- HTTP: 165 alive / 67 gold
- HTTPS: 121 alive / 18 gold
- SOCKS4: 190 alive / 132 gold
- SOCKS5: 198 alive / 138 gold

## Historical pool

- Discovered: 147168
- Ever alive: 25761
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
