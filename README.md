# SyndProxy validated proxy pool

## Current pool

- Alive now: 548
- Gold now: 405
- HTTP: 109 alive / 66 gold
- HTTPS: 71 alive / 17 gold
- SOCKS4: 179 alive / 158 gold
- SOCKS5: 189 alive / 164 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38742
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
