# SyndProxy private pool

## Current pool

- Alive now: 1026
- Gold now: 435
- HTTP: 297 alive / 86 gold
- HTTPS: 233 alive / 28 gold
- SOCKS4: 239 alive / 152 gold
- SOCKS5: 257 alive / 169 gold

## Historical pool

- Discovered: 164960
- Ever alive: 32241
- Ever gold: 1177

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
