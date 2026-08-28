# SyndProxy validated proxy pool

## Current pool

- Alive now: 559
- Gold now: 413
- HTTP: 99 alive / 67 gold
- HTTPS: 104 alive / 20 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 181 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42601
- Ever gold: 1358

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
