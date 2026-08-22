# SyndProxy private pool

## Current pool

- Alive now: 897
- Gold now: 435
- HTTP: 243 alive / 98 gold
- HTTPS: 199 alive / 26 gold
- SOCKS4: 209 alive / 151 gold
- SOCKS5: 246 alive / 160 gold

## Historical pool

- Discovered: 163327
- Ever alive: 31836
- Ever gold: 1167

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
