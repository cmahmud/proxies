# SyndProxy validated proxy pool

## Current pool

- Alive now: 495
- Gold now: 393
- HTTP: 80 alive / 53 gold
- HTTPS: 72 alive / 17 gold
- SOCKS4: 169 alive / 162 gold
- SOCKS5: 174 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42899
- Ever gold: 1364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
