# SyndProxy validated proxy pool

## Current pool

- Alive now: 624
- Gold now: 423
- HTTP: 112 alive / 77 gold
- HTTPS: 137 alive / 20 gold
- SOCKS4: 181 alive / 158 gold
- SOCKS5: 194 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42364
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
