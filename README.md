# SyndProxy validated proxy pool

## Current pool

- Alive now: 614
- Gold now: 424
- HTTP: 129 alive / 74 gold
- HTTPS: 107 alive / 20 gold
- SOCKS4: 186 alive / 162 gold
- SOCKS5: 192 alive / 168 gold

## Historical pool

- Discovered: 181482
- Ever alive: 33857
- Ever gold: 1252

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
