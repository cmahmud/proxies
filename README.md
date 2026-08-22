# SyndProxy private pool

## Current pool

- Alive now: 835
- Gold now: 365
- HTTP: 270 alive / 77 gold
- HTTPS: 164 alive / 21 gold
- SOCKS4: 179 alive / 117 gold
- SOCKS5: 222 alive / 150 gold

## Historical pool

- Discovered: 166322
- Ever alive: 32389
- Ever gold: 1179

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
