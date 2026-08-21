# SyndProxy private pool

## Current pool

- Alive now: 773
- Gold now: 390
- HTTP: 253 alive / 90 gold
- HTTPS: 109 alive / 23 gold
- SOCKS4: 182 alive / 122 gold
- SOCKS5: 229 alive / 155 gold

## Historical pool

- Discovered: 156418
- Ever alive: 29470
- Ever gold: 1128

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
