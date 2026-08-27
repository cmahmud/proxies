# SyndProxy validated proxy pool

## Current pool

- Alive now: 635
- Gold now: 405
- HTTP: 100 alive / 62 gold
- HTTPS: 174 alive / 15 gold
- SOCKS4: 177 alive / 163 gold
- SOCKS5: 184 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41035
- Ever gold: 1316

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
