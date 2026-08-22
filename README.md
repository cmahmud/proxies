# SyndProxy private pool

## Current pool

- Alive now: 930
- Gold now: 410
- HTTP: 294 alive / 84 gold
- HTTPS: 173 alive / 25 gold
- SOCKS4: 210 alive / 154 gold
- SOCKS5: 253 alive / 147 gold

## Historical pool

- Discovered: 165846
- Ever alive: 32376
- Ever gold: 1179

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
