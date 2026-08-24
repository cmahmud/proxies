# SyndProxy validated proxy pool

## Current pool

- Alive now: 614
- Gold now: 422
- HTTP: 137 alive / 73 gold
- HTTPS: 106 alive / 21 gold
- SOCKS4: 186 alive / 162 gold
- SOCKS5: 185 alive / 166 gold

## Historical pool

- Discovered: 181482
- Ever alive: 33857
- Ever gold: 1252

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
