# SyndProxy private pool

## Current pool

- Alive now: 802
- Gold now: 404
- HTTP: 209 alive / 90 gold
- HTTPS: 157 alive / 29 gold
- SOCKS4: 211 alive / 131 gold
- SOCKS5: 225 alive / 154 gold

## Historical pool

- Discovered: 163842
- Ever alive: 31933
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
