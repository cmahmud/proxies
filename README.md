# SyndProxy validated proxy pool

## Current pool

- Alive now: 492
- Gold now: 379
- HTTP: 107 alive / 58 gold
- HTTPS: 32 alive / 9 gold
- SOCKS4: 169 alive / 153 gold
- SOCKS5: 184 alive / 159 gold

## Historical pool

- Discovered: 174803
- Ever alive: 33086
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
