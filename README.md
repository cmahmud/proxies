# SyndProxy validated proxy pool

## Current pool

- Alive now: 508
- Gold now: 401
- HTTP: 111 alive / 70 gold
- HTTPS: 65 alive / 27 gold
- SOCKS4: 159 alive / 149 gold
- SOCKS5: 173 alive / 155 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43654
- Ever gold: 1376

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
