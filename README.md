# SyndProxy validated proxy pool

## Current pool

- Alive now: 643
- Gold now: 405
- HTTP: 97 alive / 61 gold
- HTTPS: 181 alive / 16 gold
- SOCKS4: 178 alive / 163 gold
- SOCKS5: 187 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41034
- Ever gold: 1316

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
