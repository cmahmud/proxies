# SyndProxy private pool

## Current pool

- Alive now: 836
- Gold now: 446
- HTTP: 214 alive / 107 gold
- HTTPS: 162 alive / 28 gold
- SOCKS4: 206 alive / 152 gold
- SOCKS5: 254 alive / 159 gold

## Historical pool

- Discovered: 163327
- Ever alive: 31830
- Ever gold: 1167

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
