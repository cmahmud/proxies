# SyndProxy private pool

## Current pool

- Alive now: 851
- Gold now: 389
- HTTP: 262 alive / 80 gold
- HTTPS: 161 alive / 30 gold
- SOCKS4: 211 alive / 148 gold
- SOCKS5: 217 alive / 131 gold

## Historical pool

- Discovered: 163330
- Ever alive: 31857
- Ever gold: 1167

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
