# SyndProxy validated proxy pool

## Current pool

- Alive now: 488
- Gold now: 387
- HTTP: 78 alive / 48 gold
- HTTPS: 51 alive / 15 gold
- SOCKS4: 178 alive / 161 gold
- SOCKS5: 181 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41632
- Ever gold: 1341

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
