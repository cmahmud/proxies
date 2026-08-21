# SyndProxy private pool

## Current pool

- Alive now: 1160
- Gold now: 424
- HTTP: 387 alive / 95 gold
- HTTPS: 281 alive / 26 gold
- SOCKS4: 231 alive / 147 gold
- SOCKS5: 261 alive / 156 gold

## Historical pool

- Discovered: 152749
- Ever alive: 28236
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
