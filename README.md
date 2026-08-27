# SyndProxy validated proxy pool

## Current pool

- Alive now: 539
- Gold now: 416
- HTTP: 103 alive / 71 gold
- HTTPS: 98 alive / 24 gold
- SOCKS4: 165 alive / 160 gold
- SOCKS5: 173 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41797
- Ever gold: 1343

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
