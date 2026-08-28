# SyndProxy validated proxy pool

## Current pool

- Alive now: 574
- Gold now: 410
- HTTP: 106 alive / 66 gold
- HTTPS: 115 alive / 19 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 181 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43005
- Ever gold: 1365

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
