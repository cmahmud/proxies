# SyndProxy private pool

## Current pool

- Alive now: 794
- Gold now: 239
- HTTP: 315 alive / 40 gold
- HTTPS: 79 alive / 7 gold
- SOCKS4: 197 alive / 124 gold
- SOCKS5: 203 alive / 68 gold

## Historical pool

- Discovered: 94342
- Ever alive: 9512
- Ever gold: 364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
