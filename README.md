# SyndProxy validated proxy pool

## Current pool

- Alive now: 659
- Gold now: 410
- HTTP: 125 alive / 71 gold
- HTTPS: 170 alive / 17 gold
- SOCKS4: 175 alive / 155 gold
- SOCKS5: 189 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40482
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
