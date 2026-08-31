# SyndProxy validated proxy pool

## Current pool

- Alive now: 639
- Gold now: 449
- HTTP: 151 alive / 85 gold
- HTTPS: 109 alive / 31 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 209 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45423
- Ever gold: 1431

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
