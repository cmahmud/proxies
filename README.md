# SyndProxy validated proxy pool

## Current pool

- Alive now: 667
- Gold now: 398
- HTTP: 146 alive / 76 gold
- HTTPS: 176 alive / 25 gold
- SOCKS4: 166 alive / 147 gold
- SOCKS5: 179 alive / 150 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40063
- Ever gold: 1306

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
