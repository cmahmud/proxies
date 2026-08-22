# SyndProxy private pool

## Current pool

- Alive now: 920
- Gold now: 404
- HTTP: 288 alive / 82 gold
- HTTPS: 174 alive / 24 gold
- SOCKS4: 210 alive / 154 gold
- SOCKS5: 248 alive / 144 gold

## Historical pool

- Discovered: 165846
- Ever alive: 32376
- Ever gold: 1179

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
