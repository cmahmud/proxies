# SyndProxy validated proxy pool

## Current pool

- Alive now: 502
- Gold now: 348
- HTTP: 145 alive / 42 gold
- HTTPS: 37 alive / 9 gold
- SOCKS4: 156 alive / 152 gold
- SOCKS5: 164 alive / 145 gold

## Historical pool

- Discovered: 171087
- Ever alive: 32861
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
