# SyndProxy validated proxy pool

## Current pool

- Alive now: 560
- Gold now: 454
- HTTP: 122 alive / 86 gold
- HTTPS: 71 alive / 35 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 194 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45568
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
