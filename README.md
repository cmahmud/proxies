# SyndProxy validated proxy pool

## Current pool

- Alive now: 674
- Gold now: 405
- HTTP: 149 alive / 71 gold
- HTTPS: 161 alive / 19 gold
- SOCKS4: 173 alive / 155 gold
- SOCKS5: 191 alive / 160 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40355
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
