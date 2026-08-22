# SyndProxy private pool

## Current pool

- Alive now: 827
- Gold now: 416
- HTTP: 233 alive / 87 gold
- HTTPS: 142 alive / 23 gold
- SOCKS4: 211 alive / 141 gold
- SOCKS5: 241 alive / 165 gold

## Historical pool

- Discovered: 162003
- Ever alive: 31392
- Ever gold: 1159

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
