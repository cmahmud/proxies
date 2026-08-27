# SyndProxy validated proxy pool

## Current pool

- Alive now: 572
- Gold now: 405
- HTTP: 91 alive / 56 gold
- HTTPS: 109 alive / 19 gold
- SOCKS4: 181 alive / 166 gold
- SOCKS5: 191 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41510
- Ever gold: 1336

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
