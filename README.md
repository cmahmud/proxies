# SyndProxy validated proxy pool

## Current pool

- Alive now: 559
- Gold now: 414
- HTTP: 94 alive / 69 gold
- HTTPS: 109 alive / 20 gold
- SOCKS4: 176 alive / 161 gold
- SOCKS5: 180 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42600
- Ever gold: 1358

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
