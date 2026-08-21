# SyndProxy private pool

## Current pool

- Alive now: 751
- Gold now: 399
- HTTP: 187 alive / 86 gold
- HTTPS: 112 alive / 24 gold
- SOCKS4: 218 alive / 148 gold
- SOCKS5: 234 alive / 141 gold

## Historical pool

- Discovered: 155693
- Ever alive: 29224
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
