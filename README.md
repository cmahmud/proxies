# SyndProxy private pool

## Current pool

- Alive now: 896
- Gold now: 404
- HTTP: 270 alive / 82 gold
- HTTPS: 178 alive / 26 gold
- SOCKS4: 203 alive / 153 gold
- SOCKS5: 245 alive / 143 gold

## Historical pool

- Discovered: 165846
- Ever alive: 32376
- Ever gold: 1179

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
