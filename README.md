# SyndProxy validated proxy pool

## Current pool

- Alive now: 565
- Gold now: 400
- HTTP: 96 alive / 62 gold
- HTTPS: 101 alive / 15 gold
- SOCKS4: 179 alive / 158 gold
- SOCKS5: 189 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41424
- Ever gold: 1328

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
