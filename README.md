# SyndProxy validated proxy pool

## Current pool

- Alive now: 462
- Gold now: 400
- HTTP: 73 alive / 54 gold
- HTTPS: 40 alive / 18 gold
- SOCKS4: 169 alive / 162 gold
- SOCKS5: 180 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42856
- Ever gold: 1364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
