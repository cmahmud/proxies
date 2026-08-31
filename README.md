# SyndProxy validated proxy pool

## Current pool

- Alive now: 632
- Gold now: 445
- HTTP: 152 alive / 84 gold
- HTTPS: 96 alive / 29 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 214 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45445
- Ever gold: 1431

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
