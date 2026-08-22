# SyndProxy private pool

## Current pool

- Alive now: 775
- Gold now: 408
- HTTP: 200 alive / 91 gold
- HTTPS: 165 alive / 25 gold
- SOCKS4: 192 alive / 138 gold
- SOCKS5: 218 alive / 154 gold

## Historical pool

- Discovered: 162443
- Ever alive: 31445
- Ever gold: 1160

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
