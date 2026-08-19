# SyndProxy private pool

## Current pool

- Alive now: 1139
- Gold now: 399
- HTTP: 370 alive / 73 gold
- HTTPS: 240 alive / 13 gold
- SOCKS4: 279 alive / 155 gold
- SOCKS5: 250 alive / 158 gold

## Historical pool

- Discovered: 131118
- Ever alive: 20677
- Ever gold: 872

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
