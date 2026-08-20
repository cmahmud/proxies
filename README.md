# SyndProxy private pool

## Current pool

- Alive now: 648
- Gold now: 327
- HTTP: 177 alive / 60 gold
- HTTPS: 117 alive / 17 gold
- SOCKS4: 171 alive / 123 gold
- SOCKS5: 183 alive / 127 gold

## Historical pool

- Discovered: 146668
- Ever alive: 25755
- Ever gold: 1075

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
