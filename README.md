# SyndProxy validated proxy pool

## Current pool

- Alive now: 645
- Gold now: 487
- HTTP: 152 alive / 102 gold
- HTTPS: 125 alive / 43 gold
- SOCKS4: 168 alive / 163 gold
- SOCKS5: 200 alive / 179 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44982
- Ever gold: 1421

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
