# SyndProxy validated proxy pool

## Current pool

- Alive now: 531
- Gold now: 414
- HTTP: 105 alive / 70 gold
- HTTPS: 85 alive / 23 gold
- SOCKS4: 168 alive / 160 gold
- SOCKS5: 173 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41775
- Ever gold: 1343

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
