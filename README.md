# SyndProxy validated proxy pool

## Current pool

- Alive now: 666
- Gold now: 398
- HTTP: 138 alive / 74 gold
- HTTPS: 181 alive / 24 gold
- SOCKS4: 168 alive / 147 gold
- SOCKS5: 179 alive / 153 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40059
- Ever gold: 1306

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
