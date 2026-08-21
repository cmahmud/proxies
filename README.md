# SyndProxy private pool

## Current pool

- Alive now: 818
- Gold now: 417
- HTTP: 244 alive / 87 gold
- HTTPS: 136 alive / 22 gold
- SOCKS4: 213 alive / 149 gold
- SOCKS5: 225 alive / 159 gold

## Historical pool

- Discovered: 156417
- Ever alive: 29457
- Ever gold: 1127

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
