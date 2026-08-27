# SyndProxy validated proxy pool

## Current pool

- Alive now: 526
- Gold now: 421
- HTTP: 103 alive / 73 gold
- HTTPS: 80 alive / 25 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 170 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41774
- Ever gold: 1343

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
