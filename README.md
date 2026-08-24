# SyndProxy validated proxy pool

## Current pool

- Alive now: 613
- Gold now: 425
- HTTP: 161 alive / 75 gold
- HTTPS: 77 alive / 22 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 202 alive / 166 gold

## Historical pool

- Discovered: 181482
- Ever alive: 33876
- Ever gold: 1252

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
