# SyndProxy validated proxy pool

## Current pool

- Alive now: 506
- Gold now: 422
- HTTP: 113 alive / 78 gold
- HTTPS: 60 alive / 29 gold
- SOCKS4: 160 alive / 154 gold
- SOCKS5: 173 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43655
- Ever gold: 1376

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
