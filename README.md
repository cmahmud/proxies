# SyndProxy validated proxy pool

## Current pool

- Alive now: 525
- Gold now: 420
- HTTP: 84 alive / 61 gold
- HTTPS: 69 alive / 22 gold
- SOCKS4: 179 alive / 163 gold
- SOCKS5: 193 alive / 174 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36113
- Ever gold: 1267

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
