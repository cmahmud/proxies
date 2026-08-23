# SyndProxy validated proxy pool

## Current pool

- Alive now: 531
- Gold now: 370
- HTTP: 98 alive / 46 gold
- HTTPS: 37 alive / 11 gold
- SOCKS4: 185 alive / 155 gold
- SOCKS5: 211 alive / 158 gold

## Historical pool

- Discovered: 173050
- Ever alive: 32993
- Ever gold: 1222

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
