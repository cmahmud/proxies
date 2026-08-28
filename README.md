# SyndProxy validated proxy pool

## Current pool

- Alive now: 537
- Gold now: 413
- HTTP: 92 alive / 65 gold
- HTTPS: 86 alive / 21 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 189 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42685
- Ever gold: 1359

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
