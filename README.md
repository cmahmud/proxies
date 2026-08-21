# SyndProxy private pool

## Current pool

- Alive now: 890
- Gold now: 375
- HTTP: 258 alive / 86 gold
- HTTPS: 216 alive / 30 gold
- SOCKS4: 188 alive / 121 gold
- SOCKS5: 228 alive / 138 gold

## Historical pool

- Discovered: 153751
- Ever alive: 28842
- Ever gold: 1114

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
