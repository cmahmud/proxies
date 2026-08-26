# SyndProxy validated proxy pool

## Current pool

- Alive now: 662
- Gold now: 396
- HTTP: 141 alive / 73 gold
- HTTPS: 178 alive / 23 gold
- SOCKS4: 166 alive / 147 gold
- SOCKS5: 177 alive / 153 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40055
- Ever gold: 1306

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
