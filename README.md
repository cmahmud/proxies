# SyndProxy validated proxy pool

## Current pool

- Alive now: 525
- Gold now: 424
- HTTP: 120 alive / 81 gold
- HTTPS: 71 alive / 28 gold
- SOCKS4: 160 alive / 155 gold
- SOCKS5: 174 alive / 160 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43656
- Ever gold: 1376

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
