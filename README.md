# SyndProxy validated proxy pool

## Current pool

- Alive now: 573
- Gold now: 448
- HTTP: 118 alive / 86 gold
- HTTPS: 79 alive / 30 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 203 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45567
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
