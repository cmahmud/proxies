# SyndProxy private pool

## Current pool

- Alive now: 839
- Gold now: 398
- HTTP: 246 alive / 96 gold
- HTTPS: 174 alive / 22 gold
- SOCKS4: 200 alive / 138 gold
- SOCKS5: 219 alive / 142 gold

## Historical pool

- Discovered: 162755
- Ever alive: 31578
- Ever gold: 1161

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
