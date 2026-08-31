# SyndProxy validated proxy pool

## Current pool

- Alive now: 580
- Gold now: 448
- HTTP: 122 alive / 84 gold
- HTTPS: 79 alive / 32 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 205 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45567
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
