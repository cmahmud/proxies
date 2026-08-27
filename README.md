# SyndProxy validated proxy pool

## Current pool

- Alive now: 566
- Gold now: 413
- HTTP: 114 alive / 72 gold
- HTTPS: 110 alive / 22 gold
- SOCKS4: 165 alive / 158 gold
- SOCKS5: 177 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41871
- Ever gold: 1344

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
