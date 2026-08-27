# SyndProxy validated proxy pool

## Current pool

- Alive now: 627
- Gold now: 419
- HTTP: 109 alive / 72 gold
- HTTPS: 158 alive / 19 gold
- SOCKS4: 181 alive / 161 gold
- SOCKS5: 179 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40965
- Ever gold: 1313

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
