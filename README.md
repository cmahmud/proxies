# SyndProxy validated proxy pool

## Current pool

- Alive now: 550
- Gold now: 413
- HTTP: 94 alive / 73 gold
- HTTPS: 107 alive / 18 gold
- SOCKS4: 171 alive / 157 gold
- SOCKS5: 178 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42055
- Ever gold: 1348

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
