# SyndProxy validated proxy pool

## Current pool

- Alive now: 525
- Gold now: 401
- HTTP: 108 alive / 75 gold
- HTTPS: 82 alive / 11 gold
- SOCKS4: 164 alive / 155 gold
- SOCKS5: 171 alive / 160 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43083
- Ever gold: 1365

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
