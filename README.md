# SyndProxy validated proxy pool

## Current pool

- Alive now: 534
- Gold now: 416
- HTTP: 102 alive / 70 gold
- HTTPS: 81 alive / 23 gold
- SOCKS4: 164 alive / 157 gold
- SOCKS5: 187 alive / 166 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34984
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
