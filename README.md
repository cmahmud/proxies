# SyndProxy validated proxy pool

## Current pool

- Alive now: 646
- Gold now: 488
- HTTP: 152 alive / 103 gold
- HTTPS: 124 alive / 43 gold
- SOCKS4: 168 alive / 163 gold
- SOCKS5: 202 alive / 179 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44982
- Ever gold: 1421

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
