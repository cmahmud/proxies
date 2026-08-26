# SyndProxy validated proxy pool

## Current pool

- Alive now: 535
- Gold now: 413
- HTTP: 102 alive / 69 gold
- HTTPS: 88 alive / 21 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 172 alive / 162 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37796
- Ever gold: 1288

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
