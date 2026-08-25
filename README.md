# SyndProxy validated proxy pool

## Current pool

- Alive now: 531
- Gold now: 416
- HTTP: 89 alive / 59 gold
- HTTPS: 81 alive / 19 gold
- SOCKS4: 171 alive / 163 gold
- SOCKS5: 190 alive / 175 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36152
- Ever gold: 1268

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
