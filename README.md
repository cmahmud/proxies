# SyndProxy validated proxy pool

## Current pool

- Alive now: 517
- Gold now: 404
- HTTP: 78 alive / 57 gold
- HTTPS: 91 alive / 20 gold
- SOCKS4: 171 alive / 163 gold
- SOCKS5: 177 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42955
- Ever gold: 1364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
