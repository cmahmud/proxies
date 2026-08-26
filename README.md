# SyndProxy validated proxy pool

## Current pool

- Alive now: 630
- Gold now: 401
- HTTP: 125 alive / 75 gold
- HTTPS: 163 alive / 25 gold
- SOCKS4: 163 alive / 148 gold
- SOCKS5: 179 alive / 153 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40112
- Ever gold: 1306

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
