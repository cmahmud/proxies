# SyndProxy private pool

## Current pool

- Alive now: 685
- Gold now: 392
- HTTP: 195 alive / 67 gold
- HTTPS: 95 alive / 21 gold
- SOCKS4: 189 alive / 150 gold
- SOCKS5: 206 alive / 154 gold

## Historical pool

- Discovered: 146668
- Ever alive: 25753
- Ever gold: 1075

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
