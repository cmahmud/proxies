# SyndProxy private pool

## Current pool

- Alive now: 862
- Gold now: 385
- HTTP: 272 alive / 80 gold
- HTTPS: 198 alive / 26 gold
- SOCKS4: 191 alive / 130 gold
- SOCKS5: 201 alive / 149 gold

## Historical pool

- Discovered: 161996
- Ever alive: 31347
- Ever gold: 1158

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
