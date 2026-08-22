# SyndProxy private pool

## Current pool

- Alive now: 965
- Gold now: 424
- HTTP: 327 alive / 87 gold
- HTTPS: 214 alive / 30 gold
- SOCKS4: 195 alive / 141 gold
- SOCKS5: 229 alive / 166 gold

## Historical pool

- Discovered: 163875
- Ever alive: 32027
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
