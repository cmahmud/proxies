# SyndProxy validated proxy pool

## Current pool

- Alive now: 520
- Gold now: 401
- HTTP: 97 alive / 60 gold
- HTTPS: 53 alive / 18 gold
- SOCKS4: 181 alive / 161 gold
- SOCKS5: 189 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41704
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
