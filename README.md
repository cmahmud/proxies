# SyndProxy validated proxy pool

## Current pool

- Alive now: 568
- Gold now: 415
- HTTP: 98 alive / 72 gold
- HTTPS: 120 alive / 19 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 181 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41945
- Ever gold: 1344

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
