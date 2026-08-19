# SyndProxy private pool

## Current pool

- Alive now: 1156
- Gold now: 543
- HTTP: 427 alive / 164 gold
- HTTPS: 285 alive / 93 gold
- SOCKS4: 217 alive / 133 gold
- SOCKS5: 227 alive / 153 gold

## Historical pool

- Discovered: 123091
- Ever alive: 18753
- Ever gold: 728

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
