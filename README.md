# SyndProxy validated proxy pool

## Current pool

- Alive now: 550
- Gold now: 404
- HTTP: 91 alive / 58 gold
- HTTPS: 85 alive / 15 gold
- SOCKS4: 179 alive / 165 gold
- SOCKS5: 195 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41550
- Ever gold: 1337

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
