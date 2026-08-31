# SyndProxy validated proxy pool

## Current pool

- Alive now: 643
- Gold now: 445
- HTTP: 145 alive / 81 gold
- HTTPS: 103 alive / 30 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 218 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45446
- Ever gold: 1432

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
