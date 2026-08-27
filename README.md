# SyndProxy validated proxy pool

## Current pool

- Alive now: 622
- Gold now: 404
- HTTP: 91 alive / 64 gold
- HTTPS: 163 alive / 15 gold
- SOCKS4: 179 alive / 162 gold
- SOCKS5: 189 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41042
- Ever gold: 1317

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
