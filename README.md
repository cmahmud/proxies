# SyndProxy validated proxy pool

## Current pool

- Alive now: 527
- Gold now: 407
- HTTP: 102 alive / 66 gold
- HTTPS: 77 alive / 19 gold
- SOCKS4: 166 alive / 158 gold
- SOCKS5: 182 alive / 164 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38604
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
