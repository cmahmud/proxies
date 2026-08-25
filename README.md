# SyndProxy validated proxy pool

## Current pool

- Alive now: 533
- Gold now: 414
- HTTP: 97 alive / 64 gold
- HTTPS: 77 alive / 21 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 187 alive / 168 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35511
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
