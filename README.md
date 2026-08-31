# SyndProxy validated proxy pool

## Current pool

- Alive now: 644
- Gold now: 438
- HTTP: 152 alive / 78 gold
- HTTPS: 104 alive / 29 gold
- SOCKS4: 171 alive / 158 gold
- SOCKS5: 217 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45411
- Ever gold: 1431

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
