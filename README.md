# SyndProxy validated proxy pool

## Current pool

- Alive now: 418
- Gold now: 352
- HTTP: 107 alive / 71 gold
- HTTPS: 44 alive / 21 gold
- SOCKS4: 93 alive / 89 gold
- SOCKS5: 174 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48691
- Ever gold: 1564

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
