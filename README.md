# SyndProxy validated proxy pool

## Current pool

- Alive now: 507
- Gold now: 389
- HTTP: 87 alive / 67 gold
- HTTPS: 93 alive / 10 gold
- SOCKS4: 158 alive / 154 gold
- SOCKS5: 169 alive / 158 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43145
- Ever gold: 1366

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
