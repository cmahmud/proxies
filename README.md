# SyndProxy validated proxy pool

## Current pool

- Alive now: 538
- Gold now: 401
- HTTP: 87 alive / 57 gold
- HTTPS: 106 alive / 21 gold
- SOCKS4: 174 alive / 160 gold
- SOCKS5: 171 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42974
- Ever gold: 1364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
