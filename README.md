# SyndProxy validated proxy pool

## Current pool

- Alive now: 646
- Gold now: 467
- HTTP: 145 alive / 98 gold
- HTTPS: 132 alive / 36 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 197 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45167
- Ever gold: 1424

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
