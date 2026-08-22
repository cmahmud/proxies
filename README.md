# SyndProxy private pool

## Current pool

- Alive now: 907
- Gold now: 396
- HTTP: 288 alive / 78 gold
- HTTPS: 171 alive / 21 gold
- SOCKS4: 207 alive / 150 gold
- SOCKS5: 241 alive / 147 gold

## Historical pool

- Discovered: 165846
- Ever alive: 32376
- Ever gold: 1179

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
