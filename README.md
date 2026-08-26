# SyndProxy validated proxy pool

## Current pool

- Alive now: 533
- Gold now: 413
- HTTP: 95 alive / 68 gold
- HTTPS: 94 alive / 22 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 173 alive / 162 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37791
- Ever gold: 1288

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
