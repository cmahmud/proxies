# SyndProxy validated proxy pool

## Current pool

- Alive now: 512
- Gold now: 420
- HTTP: 103 alive / 75 gold
- HTTPS: 47 alive / 25 gold
- SOCKS4: 178 alive / 159 gold
- SOCKS5: 184 alive / 161 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49485
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
