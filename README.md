# SyndProxy private pool

## Current pool

- Alive now: 768
- Gold now: 366
- HTTP: 194 alive / 67 gold
- HTTPS: 148 alive / 19 gold
- SOCKS4: 195 alive / 118 gold
- SOCKS5: 231 alive / 162 gold

## Historical pool

- Discovered: 148332
- Ever alive: 26070
- Ever gold: 1077

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
