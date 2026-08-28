# SyndProxy validated proxy pool

## Current pool

- Alive now: 534
- Gold now: 401
- HTTP: 87 alive / 59 gold
- HTTPS: 102 alive / 19 gold
- SOCKS4: 173 alive / 160 gold
- SOCKS5: 172 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42972
- Ever gold: 1364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
