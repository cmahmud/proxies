# SyndProxy private pool

## Current pool

- Alive now: 1394
- Gold now: 605
- HTTP: 539 alive / 196 gold
- HTTPS: 385 alive / 99 gold
- SOCKS4: 226 alive / 146 gold
- SOCKS5: 244 alive / 164 gold

## Historical pool

- Discovered: 138957
- Ever alive: 23410
- Ever gold: 920

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
