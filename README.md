# SyndProxy validated proxy pool

## Current pool

- Alive now: 636
- Gold now: 429
- HTTP: 113 alive / 82 gold
- HTTPS: 149 alive / 20 gold
- SOCKS4: 181 alive / 161 gold
- SOCKS5: 193 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42255
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
