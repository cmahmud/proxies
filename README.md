# SyndProxy validated proxy pool

## Current pool

- Alive now: 563
- Gold now: 353
- HTTP: 93 alive / 71 gold
- HTTPS: 61 alive / 31 gold
- SOCKS4: 199 alive / 78 gold
- SOCKS5: 210 alive / 173 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48585
- Ever gold: 1553

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
