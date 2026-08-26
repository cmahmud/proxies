# SyndProxy validated proxy pool

## Current pool

- Alive now: 638
- Gold now: 394
- HTTP: 129 alive / 73 gold
- HTTPS: 173 alive / 23 gold
- SOCKS4: 158 alive / 147 gold
- SOCKS5: 178 alive / 151 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40082
- Ever gold: 1306

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
