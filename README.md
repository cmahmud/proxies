# SyndProxy validated proxy pool

## Current pool

- Alive now: 640
- Gold now: 478
- HTTP: 145 alive / 99 gold
- HTTPS: 125 alive / 41 gold
- SOCKS4: 178 alive / 163 gold
- SOCKS5: 192 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45097
- Ever gold: 1424

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
