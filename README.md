# SyndProxy validated proxy pool

## Current pool

- Alive now: 503
- Gold now: 417
- HTTP: 111 alive / 76 gold
- HTTPS: 60 alive / 29 gold
- SOCKS4: 157 alive / 152 gold
- SOCKS5: 175 alive / 160 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43655
- Ever gold: 1376

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
