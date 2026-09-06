# SyndProxy validated proxy pool

## Current pool

- Alive now: 527
- Gold now: 391
- HTTP: 142 alive / 81 gold
- HTTPS: 54 alive / 24 gold
- SOCKS4: 155 alive / 135 gold
- SOCKS5: 176 alive / 151 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48024
- Ever gold: 1511

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
