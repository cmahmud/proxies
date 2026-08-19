# SyndProxy private pool

## Current pool

- Alive now: 1241
- Gold now: 419
- HTTP: 402 alive / 90 gold
- HTTPS: 291 alive / 23 gold
- SOCKS4: 246 alive / 140 gold
- SOCKS5: 302 alive / 166 gold

## Historical pool

- Discovered: 136183
- Ever alive: 22273
- Ever gold: 895

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
