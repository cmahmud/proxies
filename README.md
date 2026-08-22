# SyndProxy private pool

## Current pool

- Alive now: 865
- Gold now: 417
- HTTP: 225 alive / 87 gold
- HTTPS: 189 alive / 24 gold
- SOCKS4: 209 alive / 145 gold
- SOCKS5: 242 alive / 161 gold

## Historical pool

- Discovered: 163327
- Ever alive: 31845
- Ever gold: 1167

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
