# SyndProxy private pool

## Current pool

- Alive now: 776
- Gold now: 394
- HTTP: 197 alive / 85 gold
- HTTPS: 133 alive / 21 gold
- SOCKS4: 212 alive / 136 gold
- SOCKS5: 234 alive / 152 gold

## Historical pool

- Discovered: 157428
- Ever alive: 29760
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
