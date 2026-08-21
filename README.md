# SyndProxy private pool

## Current pool

- Alive now: 894
- Gold now: 383
- HTTP: 280 alive / 75 gold
- HTTPS: 174 alive / 20 gold
- SOCKS4: 212 alive / 142 gold
- SOCKS5: 228 alive / 146 gold

## Historical pool

- Discovered: 157410
- Ever alive: 29683
- Ever gold: 1136

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
