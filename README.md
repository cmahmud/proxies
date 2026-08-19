# SyndProxy private pool

## Current pool

- Alive now: 1143
- Gold now: 541
- HTTP: 428 alive / 154 gold
- HTTPS: 301 alive / 107 gold
- SOCKS4: 207 alive / 132 gold
- SOCKS5: 207 alive / 148 gold

## Historical pool

- Discovered: 127353
- Ever alive: 19836
- Ever gold: 803

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
