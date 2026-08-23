# SyndProxy validated proxy pool

## Current pool

- Alive now: 461
- Gold now: 363
- HTTP: 87 alive / 52 gold
- HTTPS: 37 alive / 11 gold
- SOCKS4: 166 alive / 151 gold
- SOCKS5: 171 alive / 149 gold

## Historical pool

- Discovered: 174123
- Ever alive: 33056
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
