# SyndProxy private pool

## Current pool

- Alive now: 874
- Gold now: 338
- HTTP: 301 alive / 63 gold
- HTTPS: 184 alive / 13 gold
- SOCKS4: 200 alive / 137 gold
- SOCKS5: 189 alive / 125 gold

## Historical pool

- Discovered: 129265
- Ever alive: 20208
- Ever gold: 864

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
