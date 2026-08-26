# SyndProxy validated proxy pool

## Current pool

- Alive now: 622
- Gold now: 399
- HTTP: 127 alive / 76 gold
- HTTPS: 157 alive / 24 gold
- SOCKS4: 161 alive / 147 gold
- SOCKS5: 177 alive / 152 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40113
- Ever gold: 1306

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
