# SyndProxy private pool

## Current pool

- Alive now: 943
- Gold now: 412
- HTTP: 279 alive / 85 gold
- HTTPS: 211 alive / 26 gold
- SOCKS4: 219 alive / 143 gold
- SOCKS5: 234 alive / 158 gold

## Historical pool

- Discovered: 159211
- Ever alive: 30189
- Ever gold: 1143

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
