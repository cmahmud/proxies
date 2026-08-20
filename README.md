# SyndProxy private pool

## Current pool

- Alive now: 711
- Gold now: 375
- HTTP: 202 alive / 75 gold
- HTTPS: 95 alive / 15 gold
- SOCKS4: 216 alive / 143 gold
- SOCKS5: 198 alive / 142 gold

## Historical pool

- Discovered: 145552
- Ever alive: 25432
- Ever gold: 1059

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
