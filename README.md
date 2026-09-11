# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 432
- HTTP: 95 alive / 76 gold
- HTTPS: 53 alive / 28 gold
- SOCKS4: 187 alive / 163 gold
- SOCKS5: 180 alive / 165 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49129
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
