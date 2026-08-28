# SyndProxy validated proxy pool

## Current pool

- Alive now: 476
- Gold now: 403
- HTTP: 83 alive / 59 gold
- HTTPS: 45 alive / 16 gold
- SOCKS4: 168 alive / 162 gold
- SOCKS5: 180 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42850
- Ever gold: 1363

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
