# SyndProxy validated proxy pool

## Current pool

- Alive now: 647
- Gold now: 404
- HTTP: 112 alive / 65 gold
- HTTPS: 173 alive / 13 gold
- SOCKS4: 180 alive / 162 gold
- SOCKS5: 182 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41185
- Ever gold: 1317

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
