# SyndProxy validated proxy pool

## Current pool

- Alive now: 587
- Gold now: 436
- HTTP: 137 alive / 82 gold
- HTTPS: 91 alive / 22 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 189 alive / 171 gold

## Historical pool

- Discovered: 181494
- Ever alive: 33981
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
