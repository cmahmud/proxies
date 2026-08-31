# SyndProxy validated proxy pool

## Current pool

- Alive now: 532
- Gold now: 408
- HTTP: 99 alive / 54 gold
- HTTPS: 69 alive / 26 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 193 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45507
- Ever gold: 1435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
