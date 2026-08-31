# SyndProxy validated proxy pool

## Current pool

- Alive now: 637
- Gold now: 445
- HTTP: 148 alive / 78 gold
- HTTPS: 98 alive / 34 gold
- SOCKS4: 167 alive / 160 gold
- SOCKS5: 224 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45440
- Ever gold: 1431

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
