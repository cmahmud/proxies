# SyndProxy private pool

## Current pool

- Alive now: 918
- Gold now: 438
- HTTP: 247 alive / 100 gold
- HTTPS: 199 alive / 27 gold
- SOCKS4: 217 alive / 151 gold
- SOCKS5: 255 alive / 160 gold

## Historical pool

- Discovered: 163327
- Ever alive: 31835
- Ever gold: 1167

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
