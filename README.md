# SyndProxy validated proxy pool

## Current pool

- Alive now: 495
- Gold now: 389
- HTTP: 88 alive / 69 gold
- HTTPS: 77 alive / 11 gold
- SOCKS4: 163 alive / 154 gold
- SOCKS5: 167 alive / 155 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43169
- Ever gold: 1366

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
