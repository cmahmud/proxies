# SyndProxy validated proxy pool

## Current pool

- Alive now: 569
- Gold now: 404
- HTTP: 100 alive / 66 gold
- HTTPS: 118 alive / 19 gold
- SOCKS4: 171 alive / 158 gold
- SOCKS5: 180 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43010
- Ever gold: 1365

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
