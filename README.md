# SyndProxy validated proxy pool

## Current pool

- Alive now: 624
- Gold now: 422
- HTTP: 145 alive / 74 gold
- HTTPS: 107 alive / 21 gold
- SOCKS4: 187 alive / 161 gold
- SOCKS5: 185 alive / 166 gold

## Historical pool

- Discovered: 181482
- Ever alive: 33857
- Ever gold: 1252

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
