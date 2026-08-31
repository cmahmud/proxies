# SyndProxy validated proxy pool

## Current pool

- Alive now: 605
- Gold now: 458
- HTTP: 127 alive / 86 gold
- HTTPS: 116 alive / 37 gold
- SOCKS4: 168 alive / 162 gold
- SOCKS5: 194 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45621
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
