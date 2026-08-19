# SyndProxy private pool

## Current pool

- Alive now: 899
- Gold now: 330
- HTTP: 291 alive / 63 gold
- HTTPS: 185 alive / 15 gold
- SOCKS4: 203 alive / 123 gold
- SOCKS5: 220 alive / 129 gold

## Historical pool

- Discovered: 129246
- Ever alive: 20123
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
