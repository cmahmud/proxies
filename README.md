# SyndProxy validated proxy pool

## Current pool

- Alive now: 660
- Gold now: 401
- HTTP: 146 alive / 74 gold
- HTTPS: 173 alive / 26 gold
- SOCKS4: 162 alive / 147 gold
- SOCKS5: 179 alive / 154 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40038
- Ever gold: 1306

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
