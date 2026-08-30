# SyndProxy validated proxy pool

## Current pool

- Alive now: 619
- Gold now: 456
- HTTP: 132 alive / 86 gold
- HTTPS: 117 alive / 37 gold
- SOCKS4: 165 alive / 160 gold
- SOCKS5: 205 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44788
- Ever gold: 1413

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
