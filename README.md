# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 428
- HTTP: 93 alive / 71 gold
- HTTPS: 37 alive / 20 gold
- SOCKS4: 189 alive / 163 gold
- SOCKS5: 200 alive / 174 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48922
- Ever gold: 1568

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
