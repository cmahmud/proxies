# SyndProxy validated proxy pool

## Current pool

- Alive now: 649
- Gold now: 398
- HTTP: 127 alive / 75 gold
- HTTPS: 185 alive / 23 gold
- SOCKS4: 162 alive / 145 gold
- SOCKS5: 175 alive / 155 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39990
- Ever gold: 1305

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
