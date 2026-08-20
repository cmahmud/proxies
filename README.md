# SyndProxy private pool

## Current pool

- Alive now: 747
- Gold now: 361
- HTTP: 210 alive / 80 gold
- HTTPS: 165 alive / 20 gold
- SOCKS4: 205 alive / 143 gold
- SOCKS5: 167 alive / 118 gold

## Historical pool

- Discovered: 145543
- Ever alive: 25342
- Ever gold: 1058

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
