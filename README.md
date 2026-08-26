# SyndProxy validated proxy pool

## Current pool

- Alive now: 634
- Gold now: 394
- HTTP: 130 alive / 73 gold
- HTTPS: 169 alive / 24 gold
- SOCKS4: 158 alive / 147 gold
- SOCKS5: 177 alive / 150 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40077
- Ever gold: 1306

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
