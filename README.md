# SyndProxy validated proxy pool

## Current pool

- Alive now: 508
- Gold now: 401
- HTTP: 106 alive / 77 gold
- HTTPS: 76 alive / 12 gold
- SOCKS4: 157 alive / 154 gold
- SOCKS5: 169 alive / 158 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43118
- Ever gold: 1366

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
