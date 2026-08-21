# SyndProxy private pool

## Current pool

- Alive now: 958
- Gold now: 405
- HTTP: 302 alive / 97 gold
- HTTPS: 212 alive / 22 gold
- SOCKS4: 187 alive / 135 gold
- SOCKS5: 257 alive / 151 gold

## Historical pool

- Discovered: 152167
- Ever alive: 27900
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
