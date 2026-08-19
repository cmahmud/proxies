# SyndProxy private pool

## Current pool

- Alive now: 1112
- Gold now: 542
- HTTP: 413 alive / 154 gold
- HTTPS: 271 alive / 108 gold
- SOCKS4: 221 alive / 138 gold
- SOCKS5: 207 alive / 142 gold

## Historical pool

- Discovered: 127353
- Ever alive: 19836
- Ever gold: 803

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
