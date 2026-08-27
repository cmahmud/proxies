# SyndProxy validated proxy pool

## Current pool

- Alive now: 604
- Gold now: 404
- HTTP: 111 alive / 62 gold
- HTTPS: 132 alive / 17 gold
- SOCKS4: 176 alive / 161 gold
- SOCKS5: 185 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41349
- Ever gold: 1326

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
