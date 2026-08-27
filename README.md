# SyndProxy validated proxy pool

## Current pool

- Alive now: 490
- Gold now: 403
- HTTP: 75 alive / 56 gold
- HTTPS: 53 alive / 19 gold
- SOCKS4: 181 alive / 164 gold
- SOCKS5: 181 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41598
- Ever gold: 1339

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
