# SyndProxy private pool

## Current pool

- Alive now: 825
- Gold now: 412
- HTTP: 241 alive / 90 gold
- HTTPS: 174 alive / 24 gold
- SOCKS4: 188 alive / 140 gold
- SOCKS5: 222 alive / 158 gold

## Historical pool

- Discovered: 162701
- Ever alive: 31450
- Ever gold: 1160

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
