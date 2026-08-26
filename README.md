# SyndProxy validated proxy pool

## Current pool

- Alive now: 620
- Gold now: 391
- HTTP: 115 alive / 69 gold
- HTTPS: 148 alive / 21 gold
- SOCKS4: 168 alive / 147 gold
- SOCKS5: 189 alive / 154 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39624
- Ever gold: 1300

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
