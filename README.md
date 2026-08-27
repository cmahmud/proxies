# SyndProxy validated proxy pool

## Current pool

- Alive now: 598
- Gold now: 417
- HTTP: 106 alive / 70 gold
- HTTPS: 134 alive / 17 gold
- SOCKS4: 172 alive / 164 gold
- SOCKS5: 186 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41281
- Ever gold: 1320

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
