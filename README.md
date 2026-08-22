# SyndProxy private pool

## Current pool

- Alive now: 804
- Gold now: 422
- HTTP: 214 alive / 92 gold
- HTTPS: 158 alive / 28 gold
- SOCKS4: 197 alive / 144 gold
- SOCKS5: 235 alive / 158 gold

## Historical pool

- Discovered: 163327
- Ever alive: 31850
- Ever gold: 1167

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
