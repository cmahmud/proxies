# SyndProxy validated proxy pool

## Current pool

- Alive now: 509
- Gold now: 373
- HTTP: 111 alive / 46 gold
- HTTPS: 47 alive / 9 gold
- SOCKS4: 169 alive / 157 gold
- SOCKS5: 182 alive / 161 gold

## Historical pool

- Discovered: 179924
- Ever alive: 33539
- Ever gold: 1241

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
