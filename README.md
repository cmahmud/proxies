# SyndProxy validated proxy pool

## Current pool

- Alive now: 561
- Gold now: 416
- HTTP: 100 alive / 72 gold
- HTTPS: 104 alive / 18 gold
- SOCKS4: 173 alive / 160 gold
- SOCKS5: 184 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42534
- Ever gold: 1358

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
