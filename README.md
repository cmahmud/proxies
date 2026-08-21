# SyndProxy private pool

## Current pool

- Alive now: 1070
- Gold now: 424
- HTTP: 355 alive / 91 gold
- HTTPS: 240 alive / 25 gold
- SOCKS4: 240 alive / 157 gold
- SOCKS5: 235 alive / 151 gold

## Historical pool

- Discovered: 158247
- Ever alive: 30053
- Ever gold: 1140

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
