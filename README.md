# SyndProxy validated proxy pool

## Current pool

- Alive now: 485
- Gold now: 397
- HTTP: 96 alive / 65 gold
- HTTPS: 39 alive / 22 gold
- SOCKS4: 155 alive / 138 gold
- SOCKS5: 195 alive / 172 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48772
- Ever gold: 1566

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
