# SyndProxy validated proxy pool

## Current pool

- Alive now: 584
- Gold now: 423
- HTTP: 135 alive / 82 gold
- HTTPS: 84 alive / 29 gold
- SOCKS4: 158 alive / 152 gold
- SOCKS5: 207 alive / 160 gold

## Historical pool

- Discovered: 199830
- Ever alive: 43982
- Ever gold: 1383

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
