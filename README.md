# SyndProxy private pool

## Current pool

- Alive now: 923
- Gold now: 322
- HTTP: 313 alive / 56 gold
- HTTPS: 185 alive / 11 gold
- SOCKS4: 209 alive / 125 gold
- SOCKS5: 216 alive / 130 gold

## Historical pool

- Discovered: 129246
- Ever alive: 20126
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
