# SyndProxy validated proxy pool

## Current pool

- Alive now: 547
- Gold now: 413
- HTTP: 97 alive / 69 gold
- HTTPS: 98 alive / 21 gold
- SOCKS4: 173 alive / 158 gold
- SOCKS5: 179 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42613
- Ever gold: 1359

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
