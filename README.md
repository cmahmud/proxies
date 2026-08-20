# SyndProxy private pool

## Current pool

- Alive now: 665
- Gold now: 357
- HTTP: 183 alive / 69 gold
- HTTPS: 96 alive / 20 gold
- SOCKS4: 185 alive / 125 gold
- SOCKS5: 201 alive / 143 gold

## Historical pool

- Discovered: 146125
- Ever alive: 25598
- Ever gold: 1067

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
