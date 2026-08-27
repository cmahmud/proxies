# SyndProxy validated proxy pool

## Current pool

- Alive now: 633
- Gold now: 404
- HTTP: 95 alive / 61 gold
- HTTPS: 174 alive / 15 gold
- SOCKS4: 177 alive / 163 gold
- SOCKS5: 187 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41031
- Ever gold: 1316

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
