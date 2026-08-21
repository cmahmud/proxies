# SyndProxy private pool

## Current pool

- Alive now: 743
- Gold now: 389
- HTTP: 193 alive / 83 gold
- HTTPS: 126 alive / 21 gold
- SOCKS4: 212 alive / 137 gold
- SOCKS5: 212 alive / 148 gold

## Historical pool

- Discovered: 155681
- Ever alive: 29198
- Ever gold: 1124

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
