# SyndProxy private pool

## Current pool

- Alive now: 889
- Gold now: 339
- HTTP: 260 alive / 66 gold
- HTTPS: 203 alive / 14 gold
- SOCKS4: 220 alive / 142 gold
- SOCKS5: 206 alive / 117 gold

## Historical pool

- Discovered: 109955
- Ever alive: 15232
- Ever gold: 491

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
