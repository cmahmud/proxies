# SyndProxy validated proxy pool

## Current pool

- Alive now: 503
- Gold now: 422
- HTTP: 105 alive / 78 gold
- HTTPS: 49 alive / 18 gold
- SOCKS4: 163 alive / 161 gold
- SOCKS5: 186 alive / 165 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44501
- Ever gold: 1403

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
