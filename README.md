# SyndProxy validated proxy pool

## Current pool

- Alive now: 509
- Gold now: 393
- HTTP: 92 alive / 65 gold
- HTTPS: 87 alive / 13 gold
- SOCKS4: 155 alive / 154 gold
- SOCKS5: 175 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43204
- Ever gold: 1366

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
