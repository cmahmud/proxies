# SyndProxy private pool

## Current pool

- Alive now: 939
- Gold now: 411
- HTTP: 286 alive / 85 gold
- HTTPS: 207 alive / 25 gold
- SOCKS4: 212 alive / 143 gold
- SOCKS5: 234 alive / 158 gold

## Historical pool

- Discovered: 159211
- Ever alive: 30181
- Ever gold: 1143

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
