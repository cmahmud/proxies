# SyndProxy validated proxy pool

## Current pool

- Alive now: 601
- Gold now: 415
- HTTP: 117 alive / 76 gold
- HTTPS: 121 alive / 18 gold
- SOCKS4: 175 alive / 157 gold
- SOCKS5: 188 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42082
- Ever gold: 1349

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
