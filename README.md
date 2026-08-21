# SyndProxy private pool

## Current pool

- Alive now: 1015
- Gold now: 361
- HTTP: 360 alive / 81 gold
- HTTPS: 231 alive / 18 gold
- SOCKS4: 212 alive / 119 gold
- SOCKS5: 212 alive / 143 gold

## Historical pool

- Discovered: 158214
- Ever alive: 29806
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
