# SyndProxy validated proxy pool

## Current pool

- Alive now: 555
- Gold now: 420
- HTTP: 103 alive / 71 gold
- HTTPS: 95 alive / 22 gold
- SOCKS4: 178 alive / 161 gold
- SOCKS5: 179 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42616
- Ever gold: 1359

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
