# SyndProxy validated proxy pool

## Current pool

- Alive now: 497
- Gold now: 379
- HTTP: 108 alive / 59 gold
- HTTPS: 33 alive / 9 gold
- SOCKS4: 169 alive / 153 gold
- SOCKS5: 187 alive / 158 gold

## Historical pool

- Discovered: 174803
- Ever alive: 33086
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
