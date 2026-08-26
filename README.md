# SyndProxy validated proxy pool

## Current pool

- Alive now: 667
- Gold now: 413
- HTTP: 146 alive / 73 gold
- HTTPS: 161 alive / 22 gold
- SOCKS4: 172 alive / 155 gold
- SOCKS5: 188 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40363
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
