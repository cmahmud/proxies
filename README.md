# SyndProxy private pool

## Current pool

- Alive now: 641
- Gold now: 385
- HTTP: 161 alive / 68 gold
- HTTPS: 96 alive / 17 gold
- SOCKS4: 187 alive / 145 gold
- SOCKS5: 197 alive / 155 gold

## Historical pool

- Discovered: 146602
- Ever alive: 25687
- Ever gold: 1071

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
