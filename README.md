# SyndProxy validated proxy pool

## Current pool

- Alive now: 606
- Gold now: 452
- HTTP: 130 alive / 83 gold
- HTTPS: 100 alive / 33 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 203 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45590
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
