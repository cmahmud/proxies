# SyndProxy private pool

## Current pool

- Alive now: 998
- Gold now: 437
- HTTP: 311 alive / 96 gold
- HTTPS: 211 alive / 34 gold
- SOCKS4: 207 alive / 141 gold
- SOCKS5: 269 alive / 166 gold

## Historical pool

- Discovered: 161986
- Ever alive: 31268
- Ever gold: 1156

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
