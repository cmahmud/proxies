# SyndProxy validated proxy pool

## Current pool

- Alive now: 666
- Gold now: 409
- HTTP: 152 alive / 74 gold
- HTTPS: 162 alive / 21 gold
- SOCKS4: 166 alive / 156 gold
- SOCKS5: 186 alive / 158 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40348
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
