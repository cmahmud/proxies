# SyndProxy private pool

## Current pool

- Alive now: 1327
- Gold now: 582
- HTTP: 451 alive / 182 gold
- HTTPS: 334 alive / 95 gold
- SOCKS4: 241 alive / 141 gold
- SOCKS5: 301 alive / 164 gold

## Historical pool

- Discovered: 138941
- Ever alive: 23194
- Ever gold: 915

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
