# SyndProxy private pool

## Current pool

- Alive now: 719
- Gold now: 386
- HTTP: 188 alive / 62 gold
- HTTPS: 126 alive / 19 gold
- SOCKS4: 199 alive / 150 gold
- SOCKS5: 206 alive / 155 gold

## Historical pool

- Discovered: 146668
- Ever alive: 25755
- Ever gold: 1075

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
