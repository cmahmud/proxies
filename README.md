# SyndProxy validated proxy pool

## Current pool

- Alive now: 637
- Gold now: 401
- HTTP: 120 alive / 62 gold
- HTTPS: 160 alive / 13 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 188 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40866
- Ever gold: 1313

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
