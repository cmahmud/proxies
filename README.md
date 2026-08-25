# SyndProxy validated proxy pool

## Current pool

- Alive now: 540
- Gold now: 416
- HTTP: 92 alive / 60 gold
- HTTPS: 81 alive / 20 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 190 alive / 174 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36141
- Ever gold: 1268

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
