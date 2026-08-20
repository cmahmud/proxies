# SyndProxy private pool

## Current pool

- Alive now: 743
- Gold now: 403
- HTTP: 164 alive / 78 gold
- HTTPS: 139 alive / 19 gold
- SOCKS4: 222 alive / 147 gold
- SOCKS5: 218 alive / 159 gold

## Historical pool

- Discovered: 147728
- Ever alive: 25996
- Ever gold: 1077

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
