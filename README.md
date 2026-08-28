# SyndProxy validated proxy pool

## Current pool

- Alive now: 469
- Gold now: 400
- HTTP: 71 alive / 54 gold
- HTTPS: 59 alive / 23 gold
- SOCKS4: 164 alive / 160 gold
- SOCKS5: 175 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42788
- Ever gold: 1361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
