# SyndProxy validated proxy pool

## Current pool

- Alive now: 580
- Gold now: 456
- HTTP: 121 alive / 85 gold
- HTTPS: 99 alive / 35 gold
- SOCKS4: 171 alive / 163 gold
- SOCKS5: 189 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45623
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
