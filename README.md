# SyndProxy validated proxy pool

## Current pool

- Alive now: 569
- Gold now: 422
- HTTP: 102 alive / 63 gold
- HTTPS: 97 alive / 25 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 195 alive / 173 gold

## Historical pool

- Discovered: 183892
- Ever alive: 35816
- Ever gold: 1261

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
