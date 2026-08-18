# SyndProxy private pool

## Current pool

- Alive now: 877
- Gold now: 288
- HTTP: 259 alive / 45 gold
- HTTPS: 188 alive / 8 gold
- SOCKS4: 218 alive / 109 gold
- SOCKS5: 212 alive / 126 gold

## Historical pool

- Discovered: 107048
- Ever alive: 14457
- Ever gold: 465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
