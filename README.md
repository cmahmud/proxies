# SyndProxy private pool

## Current pool

- Alive now: 724
- Gold now: 375
- HTTP: 207 alive / 75 gold
- HTTPS: 95 alive / 15 gold
- SOCKS4: 223 alive / 142 gold
- SOCKS5: 199 alive / 143 gold

## Historical pool

- Discovered: 145552
- Ever alive: 25432
- Ever gold: 1059

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
