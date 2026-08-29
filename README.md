# SyndProxy validated proxy pool

## Current pool

- Alive now: 337
- Gold now: 298
- HTTP: 35 alive / 22 gold
- HTTPS: 6 alive / 0 gold
- SOCKS4: 149 alive / 143 gold
- SOCKS5: 147 alive / 133 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43627
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
