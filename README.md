# SyndProxy private pool

## Current pool

- Alive now: 873
- Gold now: 391
- HTTP: 266 alive / 92 gold
- HTTPS: 175 alive / 27 gold
- SOCKS4: 218 alive / 142 gold
- SOCKS5: 214 alive / 130 gold

## Historical pool

- Discovered: 163257
- Ever alive: 31773
- Ever gold: 1166

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
