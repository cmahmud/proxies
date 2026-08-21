# SyndProxy private pool

## Current pool

- Alive now: 1012
- Gold now: 410
- HTTP: 330 alive / 91 gold
- HTTPS: 208 alive / 27 gold
- SOCKS4: 226 alive / 146 gold
- SOCKS5: 248 alive / 146 gold

## Historical pool

- Discovered: 157419
- Ever alive: 29717
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
