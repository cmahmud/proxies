# SyndProxy private pool

## Current pool

- Alive now: 944
- Gold now: 418
- HTTP: 281 alive / 87 gold
- HTTPS: 207 alive / 26 gold
- SOCKS4: 220 alive / 142 gold
- SOCKS5: 236 alive / 163 gold

## Historical pool

- Discovered: 159211
- Ever alive: 30172
- Ever gold: 1143

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
