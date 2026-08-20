# SyndProxy private pool

## Current pool

- Alive now: 1306
- Gold now: 562
- HTTP: 486 alive / 191 gold
- HTTPS: 352 alive / 93 gold
- SOCKS4: 235 alive / 146 gold
- SOCKS5: 233 alive / 132 gold

## Historical pool

- Discovered: 137899
- Ever alive: 22930
- Ever gold: 910

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
