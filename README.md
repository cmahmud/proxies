# SyndProxy private pool

## Current pool

- Alive now: 810
- Gold now: 417
- HTTP: 208 alive / 89 gold
- HTTPS: 164 alive / 27 gold
- SOCKS4: 198 alive / 144 gold
- SOCKS5: 240 alive / 157 gold

## Historical pool

- Discovered: 163327
- Ever alive: 31849
- Ever gold: 1167

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
