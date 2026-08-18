# SyndProxy private pool

## Current pool

- Alive now: 643
- Gold now: 240
- HTTP: 166 alive / 26 gold
- HTTPS: 96 alive / 8 gold
- SOCKS4: 192 alive / 119 gold
- SOCKS5: 189 alive / 87 gold

## Historical pool

- Discovered: 86739
- Ever alive: 6883
- Ever gold: 334

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
