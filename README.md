# SyndProxy private pool

## Current pool

- Alive now: 834
- Gold now: 354
- HTTP: 264 alive / 81 gold
- HTTPS: 168 alive / 17 gold
- SOCKS4: 210 alive / 142 gold
- SOCKS5: 192 alive / 114 gold

## Historical pool

- Discovered: 119831
- Ever alive: 18339
- Ever gold: 718

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
