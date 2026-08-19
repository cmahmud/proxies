# SyndProxy private pool

## Current pool

- Alive now: 1313
- Gold now: 416
- HTTP: 425 alive / 85 gold
- HTTPS: 300 alive / 16 gold
- SOCKS4: 257 alive / 157 gold
- SOCKS5: 331 alive / 158 gold

## Historical pool

- Discovered: 134540
- Ever alive: 21975
- Ever gold: 890

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
