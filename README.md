# SyndProxy private pool

## Current pool

- Alive now: 951
- Gold now: 241
- HTTP: 359 alive / 39 gold
- HTTPS: 152 alive / 8 gold
- SOCKS4: 234 alive / 131 gold
- SOCKS5: 206 alive / 63 gold

## Historical pool

- Discovered: 94344
- Ever alive: 9651
- Ever gold: 364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
