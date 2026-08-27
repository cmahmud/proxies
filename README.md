# SyndProxy validated proxy pool

## Current pool

- Alive now: 552
- Gold now: 415
- HTTP: 100 alive / 74 gold
- HTTPS: 109 alive / 20 gold
- SOCKS4: 171 alive / 158 gold
- SOCKS5: 172 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41821
- Ever gold: 1343

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
