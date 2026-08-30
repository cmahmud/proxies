# SyndProxy validated proxy pool

## Current pool

- Alive now: 540
- Gold now: 434
- HTTP: 107 alive / 82 gold
- HTTPS: 55 alive / 24 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 205 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44553
- Ever gold: 1406

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
