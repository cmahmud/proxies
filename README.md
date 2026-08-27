# SyndProxy validated proxy pool

## Current pool

- Alive now: 666
- Gold now: 398
- HTTP: 112 alive / 58 gold
- HTTPS: 178 alive / 13 gold
- SOCKS4: 175 alive / 157 gold
- SOCKS5: 201 alive / 170 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40730
- Ever gold: 1311

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
