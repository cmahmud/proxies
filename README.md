# SyndProxy validated proxy pool

## Current pool

- Alive now: 702
- Gold now: 460
- HTTP: 165 alive / 88 gold
- HTTPS: 125 alive / 36 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 239 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45324
- Ever gold: 1429

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
