# SyndProxy validated proxy pool

## Current pool

- Alive now: 650
- Gold now: 396
- HTTP: 107 alive / 58 gold
- HTTPS: 173 alive / 13 gold
- SOCKS4: 174 alive / 156 gold
- SOCKS5: 196 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40727
- Ever gold: 1311

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
