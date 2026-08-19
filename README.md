# SyndProxy private pool

## Current pool

- Alive now: 1136
- Gold now: 532
- HTTP: 424 alive / 155 gold
- HTTPS: 257 alive / 90 gold
- SOCKS4: 235 alive / 150 gold
- SOCKS5: 220 alive / 137 gold

## Historical pool

- Discovered: 119808
- Ever alive: 18017
- Ever gold: 706

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
