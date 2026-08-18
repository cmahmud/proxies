# SyndProxy private pool

## Current pool

- Alive now: 954
- Gold now: 241
- HTTP: 368 alive / 38 gold
- HTTPS: 153 alive / 8 gold
- SOCKS4: 234 alive / 131 gold
- SOCKS5: 199 alive / 64 gold

## Historical pool

- Discovered: 94344
- Ever alive: 9652
- Ever gold: 364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
