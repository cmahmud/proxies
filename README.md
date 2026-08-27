# SyndProxy validated proxy pool

## Current pool

- Alive now: 510
- Gold now: 395
- HTTP: 84 alive / 55 gold
- HTTPS: 60 alive / 16 gold
- SOCKS4: 181 alive / 162 gold
- SOCKS5: 185 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41607
- Ever gold: 1341

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
