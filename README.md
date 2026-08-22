# SyndProxy private pool

## Current pool

- Alive now: 877
- Gold now: 437
- HTTP: 230 alive / 99 gold
- HTTPS: 189 alive / 27 gold
- SOCKS4: 210 alive / 151 gold
- SOCKS5: 248 alive / 160 gold

## Historical pool

- Discovered: 163327
- Ever alive: 31836
- Ever gold: 1167

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
