# SyndProxy validated proxy pool

## Current pool

- Alive now: 646
- Gold now: 446
- HTTP: 148 alive / 84 gold
- HTTPS: 118 alive / 30 gold
- SOCKS4: 167 alive / 161 gold
- SOCKS5: 213 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45425
- Ever gold: 1431

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
