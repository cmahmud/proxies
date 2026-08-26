# SyndProxy validated proxy pool

## Current pool

- Alive now: 627
- Gold now: 400
- HTTP: 125 alive / 75 gold
- HTTPS: 159 alive / 24 gold
- SOCKS4: 160 alive / 147 gold
- SOCKS5: 183 alive / 154 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40114
- Ever gold: 1306

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
